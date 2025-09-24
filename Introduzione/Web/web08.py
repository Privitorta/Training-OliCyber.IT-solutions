import requests

url = "http://web-08.challs.olicyber.it/login"
dati = {
    "username": "admin",
    "password": "admin"
}
risposta = requests.post(url, data=dati)
print(risposta.text)