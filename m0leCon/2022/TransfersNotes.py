# Someone said that this application would ensure the safety of all the noted transactions...
# You can connect to the remote service

from pwn import *
import re
import sys

# appena ti connetti, puoi fare 6 cose
# 1. List users
# 2. List transactions
# 3. Login
# 4. Register
# 5. List transactions by user
# 6. Exit

# logicamente guardo la lista utenti, vedo che c'è un admin e intuisco che le transazioni
# da decriptare siano le sue

# scrivo due funzioni per prendere la lista transazioni e per decriptarle

def privi_get_list_transactions(r, user):
    # chiede lista transazioni dell'utente
    r.sendline(b'5')
    r.recvuntil(b': ')
    r.sendline(user.encode())
    r.recvuntil(b'[description]\n')
    trans = r.recvuntil(b'\n\n')
    return trans.split()

def privi_find_flag(transactions):
    # decripta le transazioni e cerca la flag
    # sono tutte xorate con lo stesso byte
    key = None # byte di xor
    for i in range(1, len(transactions), 2): # prendo solo le righe con i dati
        data = bytes.fromhex(transactions[i].decode())
        if key is None:
            for e in range(256):
                candidate = xor(data, bytes([e])) # provo tutti i byte
                if b' <- ' in candidate: # se c'è la freccia, è il byte giusto
                    key = bytes([e]) # trovato il byte
                    break
        decrypted = xor(data, key).decode(errors='ignore') # decripto
        # cerco flag
        match = re.search(r"ptm\{.*?\}", decrypted)
        if match:
            return match.group(0)
    return None

def main():
    try:
        r = remote("transfers-notes.challs.olicyber.it", 11306) # connetto al servizio
        r.recvuntil(b'> ') # prompt
        transactions = privi_get_list_transactions(r, "Admin") # prendo le transazioni dell'admin
        flag = privi_find_flag(transactions) # cerco la flag
        if flag:
            print(f"Flag: {flag}") 
        else:
            print("Flag non trovata", file=sys.stderr) 
        r.close()
    except Exception as e:
        print(f"Errore {e}", file=sys.stderr) # errore generico

if __name__ == "__main__":
    main()