# La richiesta di alcune risorse può essere parametrizzata, per ottenere 
# particolari versioni della risorsa in questione. Ad esempio, un blog potrebbe 
# utilizzare un'unica risorsa per rappresentare tutti i post pubblicati 
# (che sono strutturalmente tutti uguali, differendo solo per il contenuto) 
# identificando il contenuto specifico desiderato tramite un parametro numerico id.
# L'obiettivo di questa challenge è ottenere la risorsa:
# http://web-02.challs.olicyber.it/server-records 
# specificando il parametro id con il valore flag. Si consiglia di utilizzare la parola 
# chiave params della funzione get illustrata nella challange precedente.

import requests
url = "http://web-02.challs.olicyber.it/server-records"
params = {"id": "flag"}
response = requests.get(url, params=params)
print("Status code:", response.status_code)
print("Contenuto della risposta:\n")
print(response.text)