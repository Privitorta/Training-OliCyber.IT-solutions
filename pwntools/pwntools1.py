from pwn import *
import re

# ncat software-17.challs.olicyber.it 13000
#*****************************************************************
#* Benvenuto nella prima sfida Pwntools                          *
#* Riceverai una lista di numeri, sommali e dammi il risultato   *
#* Se sarai abbastanza veloce avrai la flag                      *
#* Dovrai completare 10 steps in 10 secondi                      *
#*****************************************************************
#... Invia un qualsiasi carattere per iniziare ...
#[+] Step 1 : somma questi numeri
#[5689, -7510, 5010, -5100, -4641, -6762, -5445, 9636, 8736, 7592, -4408, 3354, 7091, -5043, 6551, -2447, -4126, -8628, -4861, -4103, -1127, -8039, 2802, -5078, -3335, -1770, 6269, 5434, 5525, -9668, 7597, -972, 1639, 685, 3151, -8731, 9637, -1402, -8713, 1120, -5599, -7385, 5266, -7327, 1552, 8941, 5820, 7143, -7368, -9376, -371, -8006, 6249, -9493, -7461, 9337, -6733, -3301, 4301, -9278, 1754, 501, 4457, -5959, -4577, 73, 1808, 4836, 5450, -2898, 8914, 9616, -1180, 4513, 7401, -9828, -8033, 4177, -24, 4635, 2683, 4793, 173, 5329, -3933, 8898, 491, -5546, -7562, 6228, 290, -8057, 7761, 5685, -5578]
#Somma? :

# devo sommare i numeri che ricevo dalla connessione tra loro
# il risultato va inviato in tempo per avere la flag
# sono 10 soluzioni da inviare in 10 secondi e ovviamente i numeri sono troppi per essere sommati a mano
# quindi uso pwntools per automatizzare il processo

def main():
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)
    r.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...")
    r.sendline(b"LESSGGGGOOOOOOOOOO")

    for i in range(11):
        while True:
            line = r.recvline().decode()
            print(line.strip())
            numbers = re.findall(r'-?\d+', line)
            if len(numbers) > 1:
                numbers = list(map(int, numbers))
                break
        result = sum(numbers)
        print(f"somma inviata da noi: {result}")
        r.sendline(str(result).encode())

    try:
        flag = r.recvline().decode().strip()
        print(f"flag: {flag}")
    except EOFError:
        pass

if __name__ == "__main__":
    main()