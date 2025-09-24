> I nostri agenti sono riusciti ad ottenere l'accesso alle app di messaggistica di un famoso criminale informatico.
> Sfortunatamente i criminali non si fidavano della crittografia delle app di messaggistica e hanno deciso di criptare le loro comunicazioni con un algoritmo creato da essi stessi.
> Fonti riportano che le loro incredibili conoscenze matematiche abbiano dato vita ad un crittosistema indecifrabile.
> Dateci un occhiata, potete trovare le loro comunicazioni su http://badatmat.challs.olicyber.it
> Sappiamo che possiamo contare su di voi.
> Formato della flag: ITASEC{chiaveNino_messaggioNino_chiaveElliot_messaggioElliot}

Beh è tutto già scritto ;)

#### Calcola le chiavi coi dati ricevuti dalla chat
Usa il tool che vuoi
```bash
log_13(371293)=5
log_13(28561)=4
```

#### Calcola la chiave condivisa
```bash
(13**5)**4 = 1208925819614629174706176
```

#### Sottrai il messaggio finale
```bash
23920026561960852065946-1208925819614629174706176=4915062787080052627145
```