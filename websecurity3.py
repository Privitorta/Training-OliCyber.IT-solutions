import requests
url = "http://web-03.challs.olicyber.it/flag"
headers = {"X-Password": "admin"}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)
print("Contenuto della risposta:\n")
print(response.text)