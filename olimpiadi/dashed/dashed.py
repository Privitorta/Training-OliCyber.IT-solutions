# dashed.py - Soluzione per la CTF Dashed di OliCyber.it
# Lo script legge un file di input che contiene blocchi di codice Morse e li decodifica in un messaggio ASCII
# La cosa da capire in questo caso era che i blocchi di codice Morse rappresentavano numeri esadecimali
# e che questi numeri dovevano essere convertiti in caratteri ASCII

# Al termine del processo, runna "python decrypt.py" nel cmd prompt per decifrare il messaggio ricevuto

import sys

# mappa morse estesa (solo i caratteri necessari per hex)
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
    
    # split sui separatori morse (--..-- è la virgola in morse)
    blocks = [block.strip() for block in content.replace('\n', ' ').split('--..--') if block.strip()]
    
    # estrae solo i blocchi validi e converti in caratteri ASCII
    bitstring = ''
    
    for block in blocks:
        parts = block.split()
        
        # deve essere esattamente 4 parti (0X + 2 cifre hex)
        if len(parts) != 4:
            continue
            
        # converte morse in hex
        hex_chars = []
        for part in parts:
            if part in morse_map:
                hex_chars.append(morse_map[part])
            else:
                break
        else:
            hex_code = ''.join(hex_chars)
            
            # deve iniziare con 0X
            if hex_code.startswith("0X"):
                try:
                    value = int(hex_code, 16)
                    # verifica che sia un valore ASCII valido e accetta solo bit
                    if 0 <= value <= 127:
                        char = chr(value)
                        if char in ['0', '1']:  # solo bit validi
                            bitstring += char
                except:
                    continue
    
    if not bitstring:
        return None
    
    # da stringa binaria a messaggio ASCII
    decoded = ''
    for i in range(0, len(bitstring), 8):
        byte = bitstring[i:i+8]
        if len(byte) == 8:
            try:
                ascii_val = int(byte, 2)
                # solo caratteri stampabili e whitespace comuni
                if 32 <= ascii_val <= 126 or ascii_val in [9, 10, 13]:
                    decoded += chr(ascii_val)
            except:
                continue
    
    return decoded

def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "dashed.txt"
    result = decode_file(filename)
    
    if result:
        print("Messaggio decifrato:")
        print(result)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()