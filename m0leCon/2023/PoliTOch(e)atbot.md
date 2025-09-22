> All my messages are encrypted with my secret key, will you be able communicate with me?
> Site: http://politocheatbot.challs.olicyber.it

Ti viene chiesto di autenticarti cifrando la stringa "I'm Rob Masters, gimme the flag!" utilizzando lo strumento fornito.
La cifratura avviene tramite AES-128 in modalità [ECB](https://it.wikipedia.org/wiki/Electronic_code_book), con blocchi da 16 byte ciascuno, quindi il testo va suddiviso in blocchi e cifrato separatamente.

Il primo blocco, "I'm Rob Masters, ", corrisponde a `1be39bf6015076ba70446ca402584e98`.
Per il secondo blocco, "gimme the flag!" basta copiare il valore già apparso nella chat precedente, ovvero `5a9f9e956559ae571c6d3989f78fda3c`.

![PoliTO ch(e)atbot](../../Assets/PoliTOch(e)atbot.png)

Unendo questi due blocchi cifrati, otterrai la flag:

**ptm{ECB_bl0cks_4re_iNd3p3ndent}**