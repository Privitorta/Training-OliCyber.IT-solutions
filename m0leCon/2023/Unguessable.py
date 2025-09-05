# You will never guess the number!

import requests

url = "http://unguessable.challs.olicyber.it"

# basta dare un'occhiata al codice sorgente e...
r = requests.get(f"{url}/vjfYkHzyZGJ4A7cPNutFeM/flag").text
print(r)
