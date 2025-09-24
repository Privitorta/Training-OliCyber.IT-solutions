> Anche se sono state intercettate le mie richieste non riuscirai mai a leggerle in chiaro!

E invece...

Dopo aver scaricato il file .pcapng, filtro tutto il traffico HTTP per non sprecare tempo. Le richieste sospette erano una certa GET /robots.txt e una GET /secret/message.php. Filtrando la richiesta a GET /robots.txt ho visto:

```bash
disallow: /secret/message.php
disallow: .ssl-key.log
```

Allora ho intuito che potevo decrittare il traffico con quella .ssl-key.log, dunque ho rifiltrato il traffico per trovarla, ho seguito il flusso HTTP, ho salvato il file coi dati grezzi e aprendo le preferenze Wireshark ho settato Protocols > TLS > (Pre)-Master-Secret log e ho selezionato il file trovato, dunque permettendo a Wireshark di decrittare le sessioni HTTP.

Non restava altro che controllare. Infatti, filtro le richieste rilevanti con un veloce `http.request.uri contains "secret"` e salvo allo stesso modo in cui ho salvato il file di prima (raw) i flussi HTTP decifrati:

```bash
/secret/3NC0d3d3_1.html 
/secret/3NC0d3d3_2.html
/secret/3NC0d3d3_3.html 
/secret/3NC0d3d3_4.html  
```

Nel dubbio li ho salvati tutti, ma poi nell'aprirli ho visto che bastavano i primi due (il primo ha la 1 parte, gli altri hanno 2, 3, 4). Ho trovato delle stringhe ben poco nascoste codificate in base64, usando `echo 'BASE64STRING' | base64 -d` ho ottenuto tutti i contenuti. Ogni blocco iniziava con `this is the first part of the secret message: ...` e la parte utile era dopo i due punti (:). In ogni caso, concatenando nell'ordine corretto encoded 1, 2, 3 e 4, ottengo la flag completa.