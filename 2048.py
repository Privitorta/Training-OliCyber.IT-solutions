# 2048.py - Soluzione per la CTF 2048 di OliCyber.it
# Lo script si connette a un server e calcola le dovute operazioni basate su comandi ricevuti
# La cosa da capire in questo caso era che non si trattava di ammazzarsi di calcoli, 
# ma far ammazzare piuttosto la tua RAM di calcoli

import socket
import re
from functools import reduce

def main():
    HOST = "2048.challs.olicyber.it"
    PORT = 10007

def calcola(line):
    try:
        parts = line.strip().split() # divide la riga in parti
        op = parts[0] # primo elemento è l'operazione
        nums = list(map(float, parts[1:])) # gli altri elementi sono i numeri da elaborare

        if op == "SOMMA":
            res = nums[0] + nums[1] # somma dei primi due numeri
        elif op == "DIFFERENZA":
            res = nums[0] - nums[1] # differenza tra i primi due numeri
        elif op == "PRODOTTO":
            res = reduce(lambda x, y: x * y, nums)
        elif op == "DIVISIONE_INTERA":
            res = nums[0] // nums[1] # divisione intera tra i primi due numeri
        elif op == "POTENZA":
            base = int(nums[0]) # base della potenza
            exp = int(nums[1]) # esponente della potenza
            res = pow(base, exp) # calcolo della potenza
        else:
            return "operazione sconosciuta" # gestisce operazioni sconosciute

        # formattazione del risultato
        if res == int(res):
            res_str = str(int(res)) # converte in intero se il risultato è un numero intero
        else:
            res_str = str(res) # converte in stringa se il risultato è un float

        # per evitare errori di formattazione, mantengo solo cifre e segno meno
        res_filtrato = ''.join(c for c in res_str if c.isdigit() or c == '-')

        return res_filtrato 

    except Exception as e:
        return f"ERRORE: {str(e)}" # gestisce eventuali errori

    with socket.create_connection((HOST, PORT)) as sock:
        buffer = ""
        while True:
            data = sock.recv(1024).decode() # riceve i dati dal server
            buffer += data # accumula i dati ricevuti
            print(data, end='') # stampa i dati ricevuti

            lines = buffer.strip().split("\n")
            for line in lines:
                if re.match(r"^(SOMMA|DIFFERENZA|PRODOTTO|DIVISIONE_INTERA|POTENZA)", line):
                    risposta = calcola(line) # calcola il risultato dell'operazione
                    print(f"→ Risposta: {risposta}") # stampa la risposta calcolata
                    sock.sendall((risposta + "\n").encode()) # invia la risposta al server
                    buffer = "" # resetta il buffer dopo aver inviato la risposta
                    break 

if __name__ == "__main__":
    main() # avvia il programma