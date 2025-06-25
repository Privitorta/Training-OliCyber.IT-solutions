# baity5.py - Soluzione per la CTF Baity5 di OliCyber.it (Windows-friendly)

binary_path = r"C:\Users\Emma\Downloads\CTF\baity5\baity5"

def extract_strings(filepath, min_length=4):
    with open(filepath, "rb") as f:
        data = f.read()
    
    strings = []
    current_string = []
    
    for byte in data:
        if 32 <= byte <= 126:  # Caratteri stampabili ASCII
            current_string.append(chr(byte))
        else:
            if len(current_string) >= min_length:
                strings.append("".join(current_string))
            current_string = []
    
    # Aggiungi l'ultima stringa se presente
    if len(current_string) >= min_length:
        strings.append("".join(current_string))
    
    return strings

# Estrai le stringhe e stampa le prime 1000
strings_output = extract_strings(binary_path)
for s in strings_output[:1000]:
    print(s)