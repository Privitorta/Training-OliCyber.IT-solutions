def decifra_cesare(text, shift):
    risultato = ""
    for c in text:
        if 'a' <= c <= 'z':
            risultato += chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            risultato += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        else:
            risultato += c
    return risultato

codice = "synt{CAESAR_ME!-l0h_T07_vG_e1tuG!}"

# prova tutti gli shift da 1 a 25
for s in range(1, 26):
    tentativo = decifra_cesare(codice, s)
    print(f"Shift {s:2d}: {tentativo}")

# ora, dovremmo avere il risultato corretto