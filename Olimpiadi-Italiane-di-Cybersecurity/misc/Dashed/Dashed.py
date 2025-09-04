
import sys

morse_map = {
    '-----': '0',
    '-..-': 'X',
    '...--': '3',
    '.----': '1',
}

def decode_file(filename):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            content = f.read().strip()
    except:
        return None
    
    blocks = [block.strip() for block in content.replace('\n', ' ').split('--..--') if block.strip()]
    
    bitstring = ''
    
    for block in blocks:
        parts = block.split()
        
        if len(parts) != 4:
            continue
            
        hex_chars = []
        for part in parts:
            if part in morse_map:
                hex_chars.append(morse_map[part])
            else:
                break
        else:
            hex_code = ''.join(hex_chars)
            
            if hex_code.startswith("0X"):
                try:
                    value = int(hex_code, 16)
                    if 0 <= value <= 127:
                        char = chr(value)
                        if char in ['0', '1']:
                            bitstring += char
                except:
                    continue
    
    if not bitstring:
        return None
    
    decoded = ''
    for i in range(0, len(bitstring), 8):
        byte = bitstring[i:i+8]
        if len(byte) == 8:
            try:
                ascii_val = int(byte, 2)
                if 32 <= ascii_val <= 126 or ascii_val in [9, 10, 13]:
                    decoded += chr(ascii_val)
            except:
                continue
    
    return decoded

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "dashed.txt"
    result = decode_file(filename)
    
    if result:
        print("messaggio decifrato:")
        print(result)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()