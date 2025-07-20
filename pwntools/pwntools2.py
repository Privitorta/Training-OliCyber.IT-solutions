from pwn import *
import re

# ncat software-17.challs.olicyber.it 13001
#*****************************************************************
#* Benvenuto nella seconda sfida Pwntools                        *
#* Riceverai una lista di numeri e dovrai restituirmeli          *
#* packed a 64 o 32 bit                                          *
#* Se sarai abbastanza veloce avrai la flag                      *
#* Dovrai completare 100 steps in 10 secondi                     *
#*****************************************************************
#... Invia un qualsiasi carattere per iniziare ...
# [+] Step 1 : restituiscimi 0x2c19a95 packed a 64-bit

def main():
    HOST = "software-17.challs.olicyber.it"
    PORT = 13001
    r = remote(HOST, PORT)
    r.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...")
    r.sendline(b"LEESGGGGOOO")

    for i in range(101):
        while True:
            try:
                line = r.recvline().decode()
            except EOFError:
                return
            print(line.strip())
            # cerco la stringa che contiene il numero da restituire
            if "packed a" in line:
                match = re.search(r'restituiscimi (0x[0-9a-fA-F]+|\d+) packed a (32|64)-bit', line)
                # se trovo la stringa
                if match:
                    num_str = match.group(1) # prendo il numero
                    bits = int(match.group(2)) # prendo il numero di bit
                    # converto il numero in un intero
                    if num_str.startswith("0x"): 
                        num = int(num_str, 16) # se il numero è esadecimale
                    else:
                        num = int(num_str) # se il numero è decimale
                    # packing
                    if bits == 64:
                        packed = p64(num) # se il numero è a 64 bit
                    else:
                        packed = p32(num) # se il numero è a 32 bit
                    print(f"risposta inviata da noi: {packed.hex()}") # stampa nostra risposta
                    r.send(packed) # invio la risposta
                    break

    try:
        flag = r.recvline().decode().strip() # ricevo la flag
        print(f"flag: {flag}") # stampa la flag
    except EOFError: # per evitare errori se il server chiude la connessione
        pass

if __name__ == "__main__":
    main()
