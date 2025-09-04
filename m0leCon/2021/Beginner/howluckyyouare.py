from pwn import *

# il seed viene sempre generato uguale
seed = 1804289383 
r = remote("lucky.challs.olicyber.it", 17000) # la port potrebbe variare
r.recv()
r.sendline(str(seed).encode())
r.recvuntil(b"ptm")
print("ptm" + r.recv().decode())