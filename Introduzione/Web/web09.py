import requests

url = "http://web-09.challs.olicyber.it/login"
dati = {
    "username": "admin",
    "password": "admin"
}
risposta = requests.post(url, json=dati)
print(risposta.text)

# flag{w31c0m3_70_7h3_y34r_2000}