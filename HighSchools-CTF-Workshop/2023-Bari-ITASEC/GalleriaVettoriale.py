# Abbiamo costruito la galleria di immagini vettoriale più gettonata 
# d'Italia, ma qualcuno ci vuole screditare agli occhi dei critici 
# ed è riuscito a inserire un'immagine di pessima qualità 
# (anche se non visibile ad occhio nudo).
# Sai dirci quale? La nostra intelligence ha rilevato che la richiesta 
# di questa immagine potrebbe essere particolare...

import requests

url = "http://vectorial.challs.olicyber.it"
flag = requests.get(f"{url}/4.jpeg")
# print(flag.headers)
if 'X-Flag' in flag.headers:
    print(flag.headers['X-Flag'])