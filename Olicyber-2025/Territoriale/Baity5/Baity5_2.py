from Baity5 import extract_strings

binary_path = r"C:\Users\Emma\Downloads\CTF\baity5\baity5"
strings_output = extract_strings(binary_path)

candidates = [s for s in strings_output if len(s) >= 40 and all(32 <= ord(c) < 127 for c in s)]

print("\nstringhe candidate (Base85):")
for i, candidate in enumerate(candidates[:10]):
    print(f"{i+1}. {candidate}")

# Se trovi una stringa promettente, copiala in baity5_3.py per la decodifica