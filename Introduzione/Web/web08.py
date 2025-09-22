import requests

url = "http://web-08.challs.olicyber.it/login"
dati = {
    "username": "admin",
    "password": "admin"
}
risposta = requests.post(url, data=dati)
print(risposta.text)

# flag{53nding_d474_7h3_01d_w4y}