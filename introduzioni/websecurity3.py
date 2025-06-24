import requests
url = "http://web-03.challs.olicyber.it/flag"
headers = {"X-Password": "admin"} # specifica l'header X-Password con il valore admin

response = requests.get(url, headers=headers) # effettua una richiesta GET all'URL specificato con l'header
print("Status code:", response.status_code)
print("Contenuto della risposta:\n")
print(response.text)