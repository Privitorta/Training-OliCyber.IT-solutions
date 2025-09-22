# Un dettaglio fondamentale per ottenere sicurezza perfetta è che la chiave sia lunga tanto quanto il messaggio.
# Nel caso in cui la chiave sia molto corta (e ripetuta, per esempio) 
# potrebbe essere possibile un attacco a forza bruta: provare tutte le chiavi candidate 
# e vedere per quale si ottiene un risultato sensato.

# In questa challenge la chiave utilizzata è lunga un solo byte. Trova il modo di decifrare il messaggio.
# Nota Bene: il testo in chiaro non comincia con l'usuale flag{ e non finisce con }!

# La flag è 'flag{' + plaintext + '}'.
# ciphertext = 104e137f425954137f74107f525511457f5468134d7f146c4c

import string

ciphertext = bytes.fromhex("104e137f425954137f74107f525511457f5468134d7f146c4c")
for key in range(256):
    plaintext = bytes([b ^ key for b in ciphertext])
    try:
        decoded = plaintext.decode()
        if all(c in string.printable for c in decoded):
            print(f"key: {key} -> {decoded}")
    except UnicodeDecodeError:
        continue

# key 32