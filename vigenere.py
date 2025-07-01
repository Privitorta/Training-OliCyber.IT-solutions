flagcifrata = "fzau{ncn_isors_cviovw_pwcqoze}"

def privi_vigenere(flagcifrata, key):
    txt = ""
    keyindex = 0
    for carattere in flagcifrata:
        if carattere.isalpha():
            base = ord('A') if carattere.isupper() else ord('a')
            shift = ord(key[keyindex % len(key)].lower()) - ord('a')
            char = chr((ord(carattere) - base - shift) % 26 + base)
            txt += char
            keyindex += 1
        else:
            txt += carattere
    return txt
key = ""
for i in range(4):
    if flagcifrata[i].isalpha():
        shift = (ord(flagcifrata[i]) - ord("flag"[i])) % 26
        key += chr(shift + ord('a'))

print(f"chiave: {key}")
print(f"flag: {privi_vigenere(flagcifrata, key)}")