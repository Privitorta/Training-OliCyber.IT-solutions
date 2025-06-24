import base64

encoded = "c3ludHtDQUVTQVJfTUUhLWwwaF9UMDdfdkdfZTF0dUchfQo=" # che è quello che si è ricevuto dal file precedente
decoded_bytes = base64.b64decode(encoded)
decoded_str = decoded_bytes.decode('utf-8', errors='ignore')
print(decoded_str)

# Noterai che il messaggio decifrato è "synt{CAESAR_ME!-l0h_T07_vG_e1tuG!}" che ancora non è la flag
# Suggerisce però un altro indizio: "CAESAR_ME" 
# che indica che, mooolto probabilmente, il messaggio è stato cifrato con una cifra di Cesare
# Quindi runna l'altro file "decrypt2.py" per procedere a cercare la flag finale

# SE NON SAI COS'è LA CIFRA DI CESARE
# La cifra di Cesare sposta ogni lettera avanti o indietro nell’alfabeto di un certo numero di posizioni (da 1 a 25)
# Bisogna provare a spostare tutte le lettere della stringa con diversi valori da 1 a 25 fino a trovare una flag plausibile