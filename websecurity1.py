import requests
url = "http://web-01.challs.olicyber.it/"
try:
    response = requests.get(url)
    print("Status code:", response.status_code)  # Controlla se la richiesta è andata a buon fine (200)
    print("Contenuto della risposta:\n")
    print(response.text)  # Stampa il contenuto della risposta
except Exception as e:
    print("Errore nella richiesta:", e)