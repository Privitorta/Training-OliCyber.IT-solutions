binary_path = r"/path/to/baity5"  # cambia questo percorso con il percorso corretto del file baity5

def extract_strings(filepath, min_length=4):
    with open(filepath, "rb") as f:
        data = f.read()
    
    strings = []
    current_string = []

    for byte in data:
        if 32 <= byte <= 126:
            current_string.append(chr(byte))
        else:
            if len(current_string) >= min_length:
                strings.append("".join(current_string))
            current_string = []
    
    if len(current_string) >= min_length:
        strings.append("".join(current_string))
    
    return strings

strings_output = extract_strings(binary_path)
for s in strings_output[:1000]:
    print(s)