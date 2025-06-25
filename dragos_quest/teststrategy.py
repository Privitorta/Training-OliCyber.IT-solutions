import random

def test_strategy():
    """Test our strategy with the example from the failed run"""
    
    seed = 303821
    N = 10
    M = 3
    
    moves = ["R", "P", "S", "L", "V"]
    win_map = {
        "R": ["S", "L"],  # Rock crushes Scissors and Lizard
        "P": ["R", "V"],  # Paper covers Rock and disproves Spock
        "S": ["P", "L"],  # Scissors cuts Paper and decapitates Lizard
        "L": ["P", "V"],  # Lizard eats Paper and poisons Spock
        "V": ["R", "S"],  # Spock vaporizes Rock and smashes Scissors
    }
    
    # Generate bot moves exactly as server does
    random.seed(seed)
    bot_moves = [moves[random.randint(0, 4)] for _ in range(N)]
    print(f"Bot moves: {bot_moves}")
    
    # Find simple optimal strategy (greedy approach)
    def find_winning_move(bot_move):
        for player_move in moves:
            if bot_move in win_map[player_move]:
                return player_move
        return "R"  # fallback
    
    optimal_moves = [find_winning_move(bot_move) for bot_move in bot_moves]
    print(f"Optimal moves: {optimal_moves}")
    
    # Count how many unique moves we need
    unique_moves = len(set(optimal_moves))
    print(f"Unique moves needed: {unique_moves}")
    print(f"Coins available: {M}")
    
    # Simple strategy: try to use the most common winning move
    from collections import Counter
    move_counts = Counter(optimal_moves)
    most_common_move = move_counts.most_common(1)[0][0]
    print(f"Most common winning move: {most_common_move} (appears {move_counts[most_common_move]} times)")
    
    # Calculate score for always playing the most common move
    simple_score = sum(1 for bot_move in bot_moves if bot_move in win_map[most_common_move])
    print(f"Score using only '{most_common_move}': {simple_score}/{N}")
    
    # Verify our previous solution
    our_previous = "RRRRRRPSVV"
    prev_score = 0
    for i, (our_move, bot_move) in enumerate(zip(our_previous, bot_moves)):
        win = bot_move in win_map[our_move]
        prev_score += win
        print(f"Round {i+1}: {our_move} vs {bot_move} = {'WIN' if win else 'LOSE'}")
    
    print(f"Previous solution score: {prev_score}/{N}")
    
    # Try optimal greedy solution
    greedy_score = 0
    for i, (our_move, bot_move) in enumerate(zip(optimal_moves, bot_moves)):
        win = bot_move in win_map[our_move]
        greedy_score += win
        print(f"Greedy {i+1}: {our_move} vs {bot_move} = {'WIN' if win else 'LOSE'}")
    
    print(f"Greedy solution score: {greedy_score}/{N}")

if __name__ == "__main__":
    test_strategy()