from pwn import *
import re

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