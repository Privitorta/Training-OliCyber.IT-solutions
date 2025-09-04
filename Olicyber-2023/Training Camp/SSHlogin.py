# Finalmente sono riuscito a intercettare il login di uno degli organizzatori
# sul loro server segretissimo! Finalmente potrò avere tutte le flag...

import os
from pwn import *
import logging
logging.disable()

# username e password trovate nel file .pcapng

HOST = "ssh.challs.olicyber.it"
PORT = 34009

conn = remote(HOST, PORT)
conn.sendline(b"gabibbo")
conn.sendline(b"p4ssw0rd_SSH_s3gr3t4")
conn.sendline(b"cd Desktop")
conn.sendline(b"cd olicyber")
conn.sendline(b"cd 2022")
conn.sendline(b"cd Olicyber_git_repository_2022")
conn.sendline(b"cd network_brutta")
conn.sendline(b"cat flag.txt")
data = conn.recvuntil(b"}").decode()
flag = "flag{"+data.split("flag{")[-1]
print(flag)