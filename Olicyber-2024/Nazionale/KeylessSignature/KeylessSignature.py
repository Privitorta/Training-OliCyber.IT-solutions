# Se non hai nessuna chiave non puoi rompere nulla... Vero?
# nc keyless.challs.olicyber.it 38300

# Hint 1: https://it.wikipedia.org/wiki/Identità_di_Bézout
# Menomale che ho preso un bel voto in algebra lineare!

import logging
import os
from pwn import remote
from hashlib import sha256

logging.disable()

def h(m): return int.from_bytes(sha256(m).digest(), "big")
# questa funzione serve a calcolare l'MCD esteso; restituisce l'MCD e i coefficienti di Bézout
def emcd(a, b):
    if a == 0: return b, 0, 1
    mcd, x1, y1 = emcd(b % a, a)
    return mcd, y1 - (b // a) * x1, x1

r = remote(os.environ.get("HOST", "keyless.challs.olicyber.it"), int(os.environ.get("PORT", 38300)))
n = int(r.recvline().split()[-2][1:-1])

r.sendlineafter(b"> ", b"3") # "Register"
r.sendlineafter(b": ", b"privitorta")  # ;)
r.sendlineafter(b": ", b"admin")
r.recvlines(2) # ignoriamo la chiave pubblica e la firma
sig_line = r.recvline() # la firma che ci serve
s1, s2 = int(sig_line.split()[-2][1:-1]), int(sig_line.split()[-1][:-1]) # s1 e la s2
target, base = h(b"Verifying myself: I am admin on OliCyber.IT"), h(b"ACK") # il target e il base
# calcoliamo i coefficienti di Bézout per (e, -target)
_, c1, c2 = emcd(65537, -target)
c1, c2 = c1 * -base, c2 * -base # moltiplichiamo per -base
s1f, s2f = pow(s1, c2, n), (s2 * pow(s1, c1, n)) % n # calcoliamo la nuova firma
# inviamo la firma
r.sendlineafter(b"> ", b"2")
r.sendlineafter(b": ", b"admin")
r.sendlineafter(b": ", str(s1f).encode())
r.sendlineafter(b": ", str(s2f).encode())
print(r.recvline()) # sbem