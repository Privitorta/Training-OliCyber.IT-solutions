from pwn import xor

i = b"\x27\x2d\x20\x26\x3a\x36\x29\x70\x2d\x72\x70\x1e\x39\x71\x33\x3c"
const = b"\xf8\x6f\x86\x83\xc3\x9c\x8b\x35\xf0\xc0\x87\x92\x2e\x41\x2b\x53"

def rot_key():
    global const
    const = const[-1:] + const[:-1]  # ruota di un byte a destra

for _ in range(16):
    i = xor(i, const)
    rot_key()

print(i.decode())