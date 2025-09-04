from pwn import *

r = remote("soundofsystem.challs.olicyber.it", 15000)
cmd = b"show_flag"
padding_length = (48 - len(cmd) % 48) % 48
padded = cmd + bytes([padding_length]) * padding_length
payload = padded[16:32] + padded[:16] + padded[32:]
r.recvuntil("> ")
r.sendline(payload)
r.interactive()