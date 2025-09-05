from bs4 import BeautifulSoup
import requests

url = "http://pianocarriera.challs.olicyber.it/piacar/"
html = requests.get(url[:url.index("piacar")]).text
soup = BeautifulSoup(html, "html.parser")
# trova la riga della tabella che contiene "Internship"
row = None
for tr in soup.find_all("tr", class_="giallo"):
    if "Internship" in tr.text:
        row = tr
        break
# estrai i valori dagli input della riga trovata
inputs = row.find_all("input", class_="noProp")
value = inputs[0]["value"]  # formato: cod_ins_cod_ins_padre-id_padre
cod_ins, rest = value.split("_", 1)
cod_ins_padre, id_padre = rest.split("-", 1)
# invia le richieste per aggiungere l'esame e confermare il piano
s = requests.Session()
s.post(url + "do_piaca.do", data={
    "event": "aggiungiEsameScelta",
    "cod_ins": cod_ins,
    "id_padre": id_padre,
    "cod_ins_padre": cod_ins_padre
})
flag = s.post(url + "home_pianocarriera.do", data={"event": "conferma"})
print(flag.text)

'''
url = "http://pianocarriera.challs.olicyber.it/piacar/"
html = requests.get(url[:url.index("piacar")]).text
finder = BeautifulSoup(html, "html.parser")
lists = finder.find_all("tr", class_="giallo")
for i in lists:
    if str(i).find("Internship") != -1:
        lists = i
        break
tag = lists.find_all("input", class_="noProp")[0]
index = str(tag).find("value=\"") + len("value=\"")
cod_ins = str(tag)[index:index+7]
index += 7 + 1
cod_ins_padre = str(tag)[index:index+7]
index += 7 + 1
id_padre = str(tag)[index:index+6]

s = requests.Session()
s.post(url + "do_piaca.do", data = {"event":"aggiungiEsameScelta", "cod_ins":cod_ins, "id_padre":id_padre, "cod_ins_padre":cod_ins_padre})
flag = s.post(url + "home_pianocarriera.do", data = {"event":"conferma"})
print(flag.text)
'''