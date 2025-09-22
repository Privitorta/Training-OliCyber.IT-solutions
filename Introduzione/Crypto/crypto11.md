se ti piace l'aritmetica modulare e teoria dei numeri è il tuo momento boss

```
privitorta@PC-EMMA:~$ nc crypto-11.challs.olicyber.it 30004

Salve! Questo è un tutorial su RSA.
Riprendiamo ciò che hai visto a lezione.
RSA è uno schema basato sull'aritmetica modulare.

Ho scelto due piccoli numeri primi. p = 11, q = 3.
Il loro prodotto sarà il modulo (n) che utilizzeremo per fare tutte le operazioni del caso.
n = ?
```
> 33
```
Corretto!

Ora, a noi interessa fare potenze modulo n: questo ci permetterà di cifrare e decifrare i nostri messaggi.
Prima di tutto scegli un numero, che sarà il nostro messaggio da cifrare.
m = ?
```
> 4

```
ϕ(n) è la funzione di Eulero: corrisponde al numero di invertibili modulo n, ossia a
quanti interi tra 1 ed n-1 sono coprimi con n. Nel caso in cui n = pq, ϕ(n) = (p-1)(q-1).
ϕ(n) = ?
```
> 20

```
Corretto!

Infatti in questo caso gli invertibili modulo n sono:
[1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 23, 25, 26, 28, 29, 31, 32], len == 20.

Nota come calcolare ϕ(n) sia possibile solo grazie alla conoscenza dei fattori di n.
Sì, in questo caso siamo anche riusciti ad elencare esplicitamente tutti gli invertibili, ma
in generale p,q sono numeri molto molto grandi e l'unico modo (efficiente) è ricorrere alla formula.

La sicurezza di RSA è fondata proprio su questo fatto: impedire a tutti i costi ad un attaccante
di fattorizzare il modulo e dunque di recuperare ϕ(n).
Per questo motivo il modulo (n) è parte della chiave pubblica, mentre la sua fattorizzazione è privata.

Torniamo a noi: potenze modulo n. Abbiamo la base m = 4, scegli un esponente.
e = ?
```
> 3
```
Ottimo! Cifra ora il messaggio scelto con l'esponente pubblico scelto: c = m^e (mod n).

Nota: in Python qualcosa come c = m**e % n non va bene. Questo perché quella riga di codice calcola
dapprima tutto m**e (che spesso diventa enorme), per poi effettuare la riduzione modulo n.
Ci sono algoritmi più efficienti: se la curiosità ti infervora, prova a cercare "esponenziazione modulare".
Altrimenti, un'occhiata veloce alla documentazione relativa alla funzione pow() potrebbe esserti d'aiuto..
c = ?
``` 
> 31
```
Corretto!

Ottimo! Hai cifrato con successo il tuo messaggio. Ora vediamo come decifrarlo.

Naturalmente, vorremmo "effettuare la radice e-esima del nostro cifrato".
Questa, come potrai ormai immaginare, non corrisponde alla radice e-esima nei numeri reali.

Viene in nostro soccorso il Teorema di Eulero:
    Dati a,n interi coprimi, allora a^ϕ(n) = 1 (mod n).

Quindi in realtà, come hai potuto vedere nelle slides, fare la radice e-esima negli interi modulo n
corrisponde ad elevare il cifrato all'inverso modulare (rispetto a ϕ(n)) dell'esponente utilizzato!

Questo è il motivo per cui GCD(e, ϕ(n)) dev'essere uguale a 1. Altrimenti non è possibile invertirlo!
L'inverso dell'esponente pubblico si chiama esponente privato. Anche lui dev'essere mantenuto segreto!
d = ?
``` 
> 7
```
Corretto!

Ottimo! Infatti pow(c,d,n) == m = True

Da qui in avanti la strada che porta ad un'implementazione sicura di RSA è lunga e tortuosa: ci sarebbero moltissime
altre cose da dire, dettagli a cui stare attenti, casi limite da evitare. Sicuramente, ora sei in possesso delle basi
che ti servono per affrontare challenge un attimino più complesse di questa. Good job! :) 
```

**flag{RSA_n0n_f4_p1u_C0s1_p4Ur4}**