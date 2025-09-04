# I am very proud of the note taking app that I developed, check it out here!
# allega un file NaaS.pcapng

import requests

# dando un'occhiata alle richieste API vedi che si possono vedere tutte le note dell'admin
url = "http://naas.challs.olicyber.it/api/debug/notes/1" # note dell'admin
r = requests.get(url)
print(r.json()["Notes"][1]['idea_name'])