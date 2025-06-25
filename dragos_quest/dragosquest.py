from pwn import *
import random
import sys
import time
import re

# Increase recursion limit as backup
sys.setrecursionlimit(10000)

# Pre-compute winning moves for speed
MOVES = ["R", "P", "S", "L", "V"]
WIN_MAP = {
    "R": ["S", "L"],
    "P": ["R", "V"], 
    "S": ["P", "L"],
    "L": ["P", "V"],
    "V": ["R", "S"],
}

# Pre-compute counter moves
COUNTER = {}
for player_move in MOVES:
    for bot_move in WIN_MAP[player_move]:
        COUNTER[bot_move] = player_move

def best_strategy_iterative(seed, N, M):
    """
    Iterative DP solution to avoid recursion depth issues
    """
    # Generate bot moves
    random.seed(seed)
    bot_moves = [MOVES[random.randint(0, 4)] for _ in range(N)]

    # Get optimal counters and check if greedy works
    optimal_counters = [COUNTER.get(bot_move, "R") for bot_move in bot_moves]
    
    # Count changes needed for greedy
    changes = sum(1 for i in range(1, len(optimal_counters)) 
                  if optimal_counters[i] != optimal_counters[i-1])
    
    if changes <= M:
        return "".join(optimal_counters)
    
    # Use iterative DP
    # dp[pos][last_move][budget] = max_score
    # We'll work backwards from the end
    
    # Initialize DP table
    dp = {}
    
    # Base case: at position N, score is 0
    for last_move in range(5):
        for budget in range(M + 1):
            dp[(N, last_move, budget)] = 0
    
    # Fill DP table backwards
    for pos in range(N - 1, -1, -1):
        for last_move in range(5):
            for budget in range(M + 1):
                best_score = 0
                
                for move_idx in range(5):
                    cost = 0 if move_idx == last_move else 1
                    if cost <= budget:
                        # Points for current round
                        points = 1 if bot_moves[pos] in WIN_MAP[MOVES[move_idx]] else 0
                        # Future points
                        future_key = (pos + 1, move_idx, budget - cost)
                        future_score = dp.get(future_key, 0)
                        total_score = points + future_score
                        best_score = max(best_score, total_score)
                
                dp[(pos, last_move, budget)] = best_score
    
    # Find best starting move
    best_start_score = -1
    best_start_move = 0
    for start_move in range(5):
        score = dp.get((0, start_move, M), 0)
        if score > best_start_score:
            best_start_score = score
            best_start_move = start_move
    
    # Reconstruct optimal path
    result = []
    pos = 0
    last_move = best_start_move
    budget = M
    
    while pos < N:
        best_move = last_move
        best_value = -1
        
        for move_idx in range(5):
            cost = 0 if move_idx == last_move else 1
            if cost <= budget:
                points = 1 if bot_moves[pos] in WIN_MAP[MOVES[move_idx]] else 0
                future_key = (pos + 1, move_idx, budget - cost)
                future_score = dp.get(future_key, 0)
                total_value = points + future_score
                
                if total_value > best_value:
                    best_value = total_value
                    best_move = move_idx
        
        result.append(MOVES[best_move])
        if best_move != last_move:
            budget -= 1
        last_move = best_move
        pos += 1
    
    return "".join(result)

def read_until_pattern(conn, patterns, timeout=30):
    """Read from connection until one of the patterns is found"""
    buffer = b""
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            data = conn.recv(1, timeout=1)
            if not data:
                break
            buffer += data
            
            decoded = buffer.decode('utf-8', errors='ignore')
            for pattern in patterns:
                if pattern in decoded:
                    return decoded
                    
        except Exception:
            continue
    
    return buffer.decode('utf-8', errors='ignore')

def extract_numbers(text):
    """Extract numbers from text more robustly"""
    numbers = re.findall(r'\b\d+\b', text)
    return [int(n) for n in numbers]

def check_for_flag(text):
    """Check for flag in text and return it if found"""
    flag_match = re.search(r'ptm\{[^}]+\}', text)
    if flag_match:
        return flag_match.group()
    return None

def main():
    try:
        print("Connecting to server...")
        conn = remote("dragos-quest.challs.olicyber.it", 18002, timeout=30)
        
        print("Connected! Waiting for menu...")
        
        # Read initial menu with more flexible approach
        initial_data = read_until_pattern(conn, [">", "choice", "menu"], timeout=20)
        print(f"Initial data: {repr(initial_data[-100:])}")
        
        # Check for flag in initial data
        flag = check_for_flag(initial_data)
        if flag:
            print(f"\n🎉🎉🎉 FLAG FOUND IN INITIAL DATA: {flag} 🎉🎉🎉")
            return
        
        # Send game choice
        conn.sendline(b"2")
        print("Sent choice: 2 (Play)")
        
        # Small delay to let server process
        time.sleep(0.5)
        
        successful_rounds = 0
        
        for round_num in range(1, 101):
            print(f"\n{'='*15} ROUND {round_num} {'='*15}")
            
            # Special attention to round 53
            if round_num == 53:
                print("🚨 SPECIAL ROUND 53 - PAYING EXTRA ATTENTION 🚨")
            
            try:
                # Read challenge with more robust approach
                challenge_data = ""
                start_time = time.time()
                
                # Keep reading until we get challenge parameters or timeout
                while time.time() - start_time < 20:
                    try:
                        line = conn.recvline(timeout=5).decode('utf-8', errors='ignore').strip()
                        challenge_data += line + "\n"
                        
                        # Check for flag immediately
                        flag = check_for_flag(line)
                        if flag:
                            print(f"🎉 FOUND FLAG IN ROUND {round_num}: {flag}")
                            print(f"\n🎉🎉🎉 FINAL FLAG: {flag} 🎉🎉🎉")
                            return
                        
                        # Also check for any special messages around round 53
                        if round_num >= 50 and round_num <= 56:
                            print(f"Round {round_num} line: {line}")
                        
                        # Try to extract challenge parameters
                        numbers = extract_numbers(line)
                        if len(numbers) >= 3:
                            seed, N, M = numbers[:3]
                            print(f"Challenge: seed={seed}, N={N}, M={M}")
                            break
                            
                        # Check if this line contains multiple numbers in the accumulated data
                        all_numbers = extract_numbers(challenge_data)
                        if len(all_numbers) >= 3:
                            seed, N, M = all_numbers[:3]
                            print(f"Challenge (accumulated): seed={seed}, N={N}, M={M}")
                            break
                            
                    except Exception as e:
                        print(f"Read error: {e}")
                        time.sleep(0.1)
                        continue
                
                else:
                    print("❌ Timeout reading challenge parameters")
                    print(f"Accumulated data: {repr(challenge_data[-200:])}")
                    
                    # Check for flag in accumulated data
                    flag = check_for_flag(challenge_data)
                    if flag:
                        print(f"🎉 FOUND FLAG IN ACCUMULATED DATA: {flag}")
                        print(f"\n🎉🎉🎉 FINAL FLAG: {flag} 🎉🎉🎉")
                        return
                    continue
                
                # Validate parameters
                if not (1 <= N <= 10000 and 0 <= M <= 1000):
                    print(f"❌ Invalid parameters: N={N}, M={M}")
                    continue
                
                # Generate strategy
                print("Computing strategy...")
                start_compute = time.time()
                strategy = best_strategy_iterative(seed, N, M)
                compute_time = time.time() - start_compute
                print(f"Strategy computed in {compute_time:.2f}s, length: {len(strategy)}")
                
                # Validate strategy length
                if len(strategy) != N:
                    print(f"❌ Strategy length mismatch: expected {N}, got {len(strategy)}")
                    continue
                
                # Send strategy
                print("Sending strategy...")
                conn.sendline(strategy.encode())
                
                # Brief pause to let server process
                time.sleep(0.1)
                
                successful_rounds += 1
                print(f"✅ Round {round_num} completed ({successful_rounds}/100)")
                
                # Check for immediate feedback, especially around round 53
                try:
                    feedback = conn.recvline(timeout=3).decode('utf-8', errors='ignore').strip()
                    if feedback:
                        print(f"Server feedback: {feedback}")
                        flag = check_for_flag(feedback)
                        if flag:
                            print(f"🎉 FOUND FLAG IN FEEDBACK: {flag}")
                            print(f"\n🎉🎉🎉 FINAL FLAG: {flag} 🎉🎉🎉")
                            return
                        
                        # Extra logging around round 53
                        if round_num >= 50 and round_num <= 56:
                            print(f"Round {round_num} feedback: {feedback}")
                except:
                    pass
                
                # Additional check for any data after round 53
                if round_num == 53:
                    print("🚨 ROUND 53 COMPLETED - CHECKING FOR SPECIAL MESSAGES 🚨")
                    try:
                        # Try to read any additional data
                        extra_data = read_until_pattern(conn, ["ptm{", "flag", "special"], timeout=5)
                        if extra_data:
                            print(f"Extra data after round 53: {extra_data}")
                            flag = check_for_flag(extra_data)
                            if flag:
                                print(f"🎉 FOUND FLAG AFTER ROUND 53: {flag}")
                                print(f"\n🎉🎉🎉 FINAL FLAG: {flag} 🎉🎉🎉")
                                return
                    except:
                        pass
                    
            except EOFError:
                print("❌ Connection closed by server")
                break
            except Exception as e:
                print(f"❌ Error in round {round_num}: {e}")
                print("Attempting to continue...")
                
                # Try to clear any pending data
                try:
                    pending_data = conn.recvline(timeout=1).decode('utf-8', errors='ignore')
                    flag = check_for_flag(pending_data)
                    if flag:
                        print(f"🎉 FOUND FLAG IN ERROR RECOVERY: {flag}")
                        print(f"\n🎉🎉🎉 FINAL FLAG: {flag} 🎉🎉🎉")
                        return
                except:
                    pass
                continue
        
        print(f"\n✅ Completed {successful_rounds} rounds successfully")
        
        # Read final output more aggressively
        print("\n" + "="*50)
        print("READING FINAL OUTPUT")
        print("="*50)
        
        # Try multiple approaches to get final output
        final_outputs = []
        
        # Approach 1: Read until pattern
        try:
            final_output1 = read_until_pattern(conn, ["ptm{", "flag", "congratulations"], timeout=15)
            final_outputs.append(final_output1)
            print(f"Final output (method 1): {final_output1}")
        except:
            pass
        
        # Approach 2: Read all remaining data
        try:
            time.sleep(1)  # Give server time to send final message
            final_output2 = conn.recvall(timeout=10).decode('utf-8', errors='ignore')
            final_outputs.append(final_output2)
            print(f"Final output (method 2): {final_output2}")
        except:
            pass
        
        # Approach 3: Try reading lines one by one
        try:
            for i in range(10):  # Try up to 10 lines
                line = conn.recvline(timeout=2).decode('utf-8', errors='ignore').strip()
                if line:
                    final_outputs.append(line)
                    print(f"Final line {i+1}: {line}")
                else:
                    break
        except:
            pass
        
        # Check all final outputs for flag
        for output in final_outputs:
            flag = check_for_flag(output)
            if flag:
                print(f"\n🎉🎉🎉 FINAL FLAG: {flag} 🎉🎉🎉")
                return
        
        print("No flag found in any final output")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        try:
            conn.close()
        except:
            pass

if __name__ == "__main__":
    main()