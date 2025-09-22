> A friend of mine told me about a peculiar bank. You gotta give it a try for me.
> This is a remote challenge, you can connect with: nc thewall.challs.olicyber.it 21007

Ci danno la connessione TCP e un file ELF. Usando [Ghidra](https://github.com/NationalSecurityAgency/ghidra) o un qualsiasi disassembler, analizzo il file dato. La flag è memorizzata nella stringa *notaflagbuffer* con un offset di 20 (`0x14`). 

[Ghidra](../../Assets/TheWall.png)
[Ghidra](../../Assets/TheWall2.png)

Vedendo questo puoi capire che inviando 21 caratteri ricevi la flag senza i primi caratteri. Connettiti, seleziona "Write note" (1), invia 21 caratteri (qualsiasi cosa) e poi seleziona "Read note" (2).

[Terminal](../../Assets/TheWall3.png)

**ptm{ju57_4n07h3r_br1ck_1n_7h3_w411}**