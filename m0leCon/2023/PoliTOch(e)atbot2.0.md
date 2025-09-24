> I've improved my encryption system you won't be able to break it this time!
> Site: http://politocheatbot2.challs.olicyber.it

Dovrebbe essere un revamp del file versione uno, "migliorato" in sicurezza: ora, chiede un [OTP](https://it.wikipedia.org/wiki/Cifrario_di_Vernam).

```
Hello, I'm PoliTO ch(e)atbot 2.0!
Hey! This is the password: (qui la password cambia sempre)
Please, encrypt it with the OTP that I gave you and send me the result. I'll give you the flag if you are right!
Remember to use the tools that I provide to you!
You can find them by clicking the button in top-right corner.
```

L'[OTP](https://it.wikipedia.org/wiki/Cifrario_di_Vernam) utilizza una chiave lunga quanto (o più del) testo da cifrare.
Qui la cifratura avviene facendo uno *XOR* tra il testo in chiaro e la chiave.
Se usi lo strumento del sito per cifrare e poi fai lo *XOR* tra testo originale e testo cifrato, ottieni la chiave usata.
Se cifri la chiave stessa dovresti ottenere solo zeri, ma noti che ogni volta che usi lo strumento, i byte della chiave aumentano di 1. Quindi, per ottenere la flag, invia lo *XOR* tra il testo in chiaro e la chiave che hai trovato, incrementata di 1 per ogni byte.

Dunque usa il tool "Encrypt" con la password come plaintext, ottieni il ciphertext, usa il tool "XOR" e inserisci la password come plaintext e il ciphertext come ciphertext; il risultato sarà la chiave usata dal sito. Incrementa ogni byte di 1 e usa di nuovo il tool "XOR", inserendo la password come plaintext e la chiave incrementata come key; il risultato è il valore da inviare al bot.

Uno script per automatizzare:

```python
# serve a convertire stringhe hex in bytes
def hex2byte(s):
	return bytes.fromhex(s)
# serve a fare lo xor
def xor(a, b):
	return bytes([x ^ y for x, y in zip(a, b)])
# valori settabili
password = input("Password: ").strip()
ciphertext = input("Ciphertext: ").strip()
# conversione
password = hex2byte(password)
ciphertext = hex2byte(ciphertext)
# la password è ottenuta facendo XOR tra il ciphertext e la chiave OTP
key = xor(password, ciphertext)
print("Chiave OTP:", key.hex())
key1 = bytes([(b + 1) % 256 for b in key])
print("Chiave incrementata di 1:", key1.hex())
result = xor(password, key1)
print("Risultato:", result.hex())
```

Dopo aver inviato il risultato, riceverai la flag.