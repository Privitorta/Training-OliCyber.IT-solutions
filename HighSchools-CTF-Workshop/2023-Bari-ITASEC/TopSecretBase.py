import base64
# Ho filtrato il traffico SMTP per vedere i pacchetti 
# che contengono "code" (codice di accesso) 
# ho trovato questo codice
code = "SVRBU0VDe24wdF9zMF9zM2NyM3RfYjRzM30=3D"
decoded_bytes = base64.b64decode(code)
decoded_str = decoded_bytes.decode('utf-8')
print(decoded_str)