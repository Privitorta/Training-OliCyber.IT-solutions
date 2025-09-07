> Il nostro amato "CinemaMagicServer" adora nascondere segreti tra i flussi di film che propone come assoluti capolavori.
> Buona caccia, e non dimenticare di prendere i popcorn!

Segui i flussi, se preferisci scorrili uno a uno, e assicurati di aver selezionato "mostra come ASCII".
Avrai gli indizi che ti servono lungo il percorso, e potrai poi unire la flag quando avrai trovato le tre parti:

#### Prima parte
```
HTTP/1.1 200 OK
Content-Length: 60
flag{http_ To find the next magical piece, check stream #33!
```
#### Seconda parte
```
HTTP/1.1 200 OK
Content-Length: 58
str3ams_ To find the next magical piece, check stream #87!
```

#### Terza parte
```
HTTP/1.1 200 OK
Content-Length: 10

4r3_m4g1c}
```

Risultato: **flag{http_str3ams_4r3_m4g1c}**