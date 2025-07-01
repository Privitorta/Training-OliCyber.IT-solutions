cifrato = "xcqv{gvyavn_zvztv_etvtddlnxcgy}"

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

# non mio
def generateKey():
    start = random.randint(1,25)
    key = "".join([alphabet[start:], alphabet[0:start]])
    return key

# non mio
def encrypt(plain, key):
    ciphertext = ""
    for k in range(len(plain)):
        character = plain[k]
 
        if ord(character) <= 90 and ord(character) >= 65: #lowercase
            i = alphabet.index(chr(ord(character)+32))
            characterEncrypted = chr(ord(key[i])-32)
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            ciphertext = "".join([ciphertext,characterEncrypted])
        elif ord(character) <= 122 and ord(character) >= 97:
            i = alphabet.index(character)
            characterEncrypted = key[i]
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            ciphertext = "".join([ciphertext,characterEncrypted])
        else:
            ciphertext = "".join([ciphertext,character])
        
    return ciphertext

def prividecrypt(ciphertext, key):
    plaintext = ""
    for k in range(len(ciphertext)):
        character = ciphertext[k]
        if ord(character) <= 90 and ord(character) >= 65:
            i = key.index(chr(ord(character)+32))
            characterDecrypted = chr(ord(alphabet[i])-32)
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            plaintext = "".join([plaintext,characterDecrypted])
        elif ord(character) <= 122 and ord(character) >= 97:
            i = key.index(character)
            characterDecrypted = alphabet[i]
            key = "".join([key[len(key)-1:],key[0:len(key)-1]])
            plaintext = "".join([plaintext,characterDecrypted])
        else:
            plaintext = "".join([plaintext,character])
    return plaintext

def privibruteforce(ciphertext):
    for start in range(1, 26):
        key = "".join([alphabet[start:], alphabet[0:start]])
        plain = prividecrypt(ciphertext, key)
        if plain.startswith("flag{") and plain.endswith("}"):
            print(f"flag trovata: {plain}\nchiave iniziale shift {start}")
            return plain

# non mio
def handle():
    plaintextFLAG = "...{...}"
    key = generateKey()
    ciphertext = encrypt(plaintextFLAG, key)
    print(ciphertext)
    return

if __name__ == "__main__":
    # handle ()
    privibruteforce(cifrato)