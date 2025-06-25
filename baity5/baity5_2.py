from baity5 import extract_strings

binary_path = r"C:\Users\Emma\Downloads\CTF\baity5\baity5"
strings_output = extract_strings(binary_path)

# Filtra le stringhe che sembrano essere flag codificate in Base85:
# - Lunghezza >= 40 caratteri
# - Solo caratteri ASCII stampabili (escludi controlli ridondanti se già fatto in extract_strings)
candidates = [s for s in strings_output if len(s) >= 40 and all(32 <= ord(c) < 127 for c in s)]

# Stampa le candidate per ispezione
print("\nStringhe candidate (Base85):")
for i, candidate in enumerate(candidates[:10]):  # Mostra solo le prime 10 per brevità
    print(f"{i+1}. {candidate}")

# Se trovi una stringa promettente, copiala in baity5_3.py per la decodifica