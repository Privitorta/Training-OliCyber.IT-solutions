import requests # importa la libreria requests per effettuare richieste HTTP
url = "http://web-01.challs.olicyber.it/" # definisce l'URL da cui ottenere i dati
try:
    response = requests.get(url) # effettua una richiesta GET all'URL specificato 
    print("Status code:", response.status_code) # stampa il codice di stato della risposta
    print("Contenuto della risposta:\n") # stampa il contenuto della risposta
    print(response.text) # stampa il testo della risposta
except Exception as e:
    print("Errore nella richiesta:", e) # gestisce eventuali eccezioni durante la richiesta