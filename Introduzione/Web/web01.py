import requests

url = "http://web-01.challs.olicyber.it/"

try:
    response = requests.get(url)
    print("Status code:", response.status_code)
    print("Contenuto della risposta:\n")
    print(response.text)
except Exception as e:
    print("Errore nella richiesta:", e)