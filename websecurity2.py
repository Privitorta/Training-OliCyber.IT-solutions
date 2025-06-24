import requests
url = "http://web-02.challs.olicyber.it/server-records"
params = {"id": "flag"} # definisce l'URL e i parametri da inviare nella richiesta

response = requests.get(url, params=params) # effettua una richiesta GET all'URL specificato con i parametri
print("Status code:", response.status_code)
print("Contenuto della risposta:\n")
print(response.text)