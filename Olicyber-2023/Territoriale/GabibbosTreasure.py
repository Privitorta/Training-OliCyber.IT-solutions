from urllib.parse import quote
import requests

url = "http://treasure.challs.olicyber.it/flag?password="
# dai un'occhiata al codice sorgente della pagina
# nello specifico, tag script index.html baby
payload = quote("Belandi, dammi la flag!")
r = requests.get(url + payload)
print(r.text)