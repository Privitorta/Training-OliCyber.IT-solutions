> Sono riuscito ad intercettare il traffico email di un appaltatore del governo.
> Puoi aiutarmi ad entrare in una delle loro basi?
> Sono sicuro che si siano scambiati il codice di accesso in una delle loro mail.

Ho filtrato il traffico SMTP per vedere i pacchetti che contengono "code" (codice di accesso) e ho trovato questo contenuto interessante tra i pochi risultati:

```html
Line-based text data: text/html (21 lines)
    <div class=3D"moz-text-plain"><pre wrap=3D"" class=3D"moz-quote-pre">\r\n
    </pre><blockquote type=3D"cite"><pre wrap=3D"" class=3D"moz-quote-pre">----=\r\n
    -Original Message-----\r\n
    From: Jayden Hoffman\r\n
    Sent: Sunday, November 04, 2012=\r\n
     1:59 PM\r\n
    To: Samuel Bailey\r\n
    Subject: Paint for the Nevada base\r\n
    \r\n
    Hi Samuel,\r\n
    Can you let Joseph that I bought the paint requested for the finishes at =\r\n
    the base. It's a 5 gallon bucket on a shelf at the back of the garage. It =\r\n
    should be delivered to the site in Nevada. The code to enter the base is =\r\n
    SVRBU0VDe24wdF9zMF9zM2NyM3RfYjRzM30=3D. The keypad is hanging on the white =\r\n
    post to the right of the gate.\r\n
    \r\n
    Thanks again.\r\n
    \r\n
    </pre></blockquote><pre =\r\n
    wrap=3D"" class=3D"moz-quote-pre">\r\n
    </pre></div>\r\n
```

La riga in questione è quella che mi sembra codificata in base64, `SVRBU0VDe24wdF9zMF9zM2NyM3RfYjRzM30=3D`. La decodifico con uno script python:

```python
import base64
# ho filtrato il traffico SMTP per vedere i pacchetti che contengono "code" (codice di accesso) e ho trovato questo codice
code = "SVRBU0VDe24wdF9zMF9zM2NyM3RfYjRzM30=3D"
decoded_bytes = base64.b64decode(code)
decoded_str = decoded_bytes.decode('utf-8')
print(decoded_str)
```