import socket
import json
import base64
import re

def bin_to_str(b):
    try:
        if not b:
            return ""
        n = int(b, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    except Exception as e:
        print(f"errore in bin_to_str: {e}")
        return ""

def str_to_bin(s):
    return ''.join(f'{ord(c):08b}' for c in s)

def str_to_bin_nozero(s):
    if not s:
        return ''
    try:
        b = bytes([ord(c) for c in s])
        return bin(int.from_bytes(b, 'big'))[2:]
    except Exception as e:
        print(f"errore in str_to_bin_nozero: {e}")
        return ""

def hex_to_str(h):
    try:
        return ''.join(chr(b) for b in bytes.fromhex(h))
    except Exception as e:
        print(f"errore in hex_to_str: {e}")
        return ""


def str_to_hex(s):
    try:
        return bytes([ord(c) for c in s]).hex()
    except Exception as e:
        print(f"errore in str_to_hex: {e}")
        return ""

def str_to_hex_nozero(s):
    try:
        result = bytes([ord(c) for c in s]).hex()
        return result
    except Exception as e:
        print(f"errore in str_to_hex_nozero: {e}")
        return ""

def base64_to_str(b64):
    try:
        return ''.join(chr(b) for b in base64.b64decode(b64))
    except Exception as e:
        print(f"errore in base64_to_str: {e}")
        return ""

def str_to_base64(s):
    try:
        return base64.b64encode(bytes([ord(c) for c in s])).decode()
    except Exception as e:
        print(f"errore in str_to_base64: {e}")
        return ""

def process_message(instruction, message):
    instr = instruction.lower()

    if "da binario" in instr:
        return bin_to_str(message)
    elif "a binario" in instr:
        if "senza lo 0b iniziale" in instr:
            return str_to_bin_nozero(message)
        else:
            return str_to_bin(message)
        
    elif "da esadecimale" in instr:
        return hex_to_str(message)
    elif "a esadecimale" in instr:
        if "senza lo 0x iniziale" in instr:
            return str_to_hex_nozero(message)
        else:
            return str_to_hex(message)
        
    elif "da base64" in instr:
        return base64_to_str(message)
    elif "a base64" in instr:
        return str_to_base64(message)
    
    else:
        return ""

def main():
    HOST = "based.challs.olicyber.it"
    PORT = 10600

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        buffer = ""
        while True:
            data = s.recv(4096).decode(errors='ignore')
            if not data:
                break
            print(data)

            buffer += data

            while True:
                json_match = re.search(r'(\{.*?\})', buffer, re.DOTALL)
                if not json_match:
                    break
                json_str = json_match.group(1)
                try:
                    obj = json.loads(json_str)
                except json.JSONDecodeError:
                    break

                message = obj.get("message", "")

                before_json = buffer[:json_match.start()]
                instr_matches = list(re.finditer(r'converti.*', before_json, re.IGNORECASE))
                if not instr_matches:
                    buffer = buffer[json_match.end():]
                    continue
                instruction = instr_matches[-1].group(0)

                answer = process_message(instruction, message)
                response = json.dumps({"answer": answer}) + "\n"
                s.sendall(response.encode())
                print(response)
                buffer = buffer[json_match.end():]

if __name__ == "__main__":
    main()
