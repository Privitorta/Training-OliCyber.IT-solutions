from pwn import *

# ncat software-17.challs.olicyber.it 13002
# *****************************************************************
# * Benvenuto nella terza sfida Pwntools                          *
# * Riceverai una lista di nomi di funzioni e dovrai resituirmi   *
# * il loro indirizzo all'interno del binario in esadecimale      *
# * Se sarai abbastanza veloce avrai la flag                      *
# * Dovrai completare 20 steps in 10 secondi                      *
# *****************************************************************
# ... Invia un qualsiasi carattere per iniziare ...
# -> x:

#context.log_level = 'error'

def privi(received: bytes, sent: bytes):
    print(f"ricevuto: {received.decode().strip()}")
    print(f"inviato: {sent.decode().strip()}")

def main():
    exe = ELF("./sw-19")
    r = remote("software-17.challs.olicyber.it", 13002)
    r.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...")
    r.sendline(b"e")

    try:
        while True:
            line = r.recvuntil(b":", timeout=2)
            if b"Ecco la flag" in line:
                flag_line = r.recvline(timeout=1)
                print("\nflag:", flag_line.decode().strip(), "\n")
                break
            if b"lento" in line or b"perso" in line:
                print("\nfallita come te:", line.decode().strip())
                break
            if b"->" in line:
                try:
                    func_name = line.decode().split("->")[1].split(":")[0].strip()
                    address = hex(exe.sym.get(func_name, 0)).encode()
                    privi(line, address)
                    r.sendline(address)
                except:
                    r.sendline(b"0x0")
    except Exception:
        pass
    r.close()

if __name__ == "__main__":
    main()






# sw-19 symbol table
'''{'stdout': 4210896, 'abi-note.c': 0, '__abi_tag': 4195048, 'init.c': 0, 'static-reloc.c': 0, 
'crtstuff.c': 0, 'deregister_tm_clones': 4198688, 'register_tm_clones': 4198736, 
'__do_global_dtors_aux': 4198800, 'completed.0': 4210904, '__do_global_dtors_aux_fini_array_entry': 4210136, 
'frame_dummy': 4198848, '__frame_dummy_init_array_entry': 4210128, 'chall.c': 0, 'func.5': 4203135, 
'func.4': 4203140, 'func.3': 4203145, 'func.2': 4203150, 'func.1': 4203154, 'func.0': 4203159, 
'FRAME_END': 4203732, '__init_array_end': 4210136, '_DYNAMIC': 4210192, '__init_array_start': 4210128, 
'__GNU_EH_FRAME_HDR': 4203164, 'GLOBAL_OFFSET_TABLE': 4210688, '__libc_csu_fini': 4199568, 
'alarm_handler': 4198964, 'addresses': 4210144, 'stdout@@GLIBC_2.2.5': 4210896, 'data_start': 4210816, 
'_edata': 4210896, '_fini': 4199572, 'dead': 4198850, '__data_start': 4210816, 'beef': 4198869, 
'__dso_handle': 4210824, '_IO_stdin_used': 4202496, '__libc_csu_init': 4199472, 'foo': 4198907, 
'_end': 4210912, '_start': 4198640, '__bss_start': 4210896, 'cafe': 4198926, 'main': 4198997, 
'bebe': 4198945, 'names': 4210848, 'c0de': 4198888, 'TMC_END': 4210896, '_init': 4198400, 
'plt.chall.c': 4198636, 'puts': 4198448, 'plt.puts': 4198448, '__stack_chk_fail': 4198464, 
'plt.__stack_chk_fail': 4198464, 'printf': 4198480, 'plt.printf': 4198480, 'alarm': 4198496, 
'plt.alarm': 4198496, 'srand': 4198512, 'plt.srand': 4198512, 'getchar': 4198528, 'plt.getchar': 4198528, 
'signal': 4198544, 'plt.signal': 4198544, 'time': 4198560, 'plt.time': 4198560, 'setvbuf': 4198576, 
'plt.setvbuf': 4198576, '__isoc99_scanf': 4198592, 'plt.__isoc99_scanf': 4198592, 'exit': 4198608, 
'plt.exit': 4198608, 'rand': 4198624, 'plt.rand': 4198624, '__libc_start_main': 4210656, 
'got.__libc_start_main': 4210656, 'gmon_start': 4210664, 'got.gmon_start': 4210664, 
'got.stdout': 4210896, 'got.puts': 4210712, 'got.__stack_chk_fail': 4210720, 'got.printf': 4210728, 
'got.alarm': 4210736, 'got.srand': 4210744, 'got.getchar': 4210752, 'got.signal': 4210760, 
'got.time': 4210768, 'got.setvbuf': 4210776, 'got.__isoc99_scanf': 4210784, 'got.exit': 4210792, 
'got.rand': 4210800}'''