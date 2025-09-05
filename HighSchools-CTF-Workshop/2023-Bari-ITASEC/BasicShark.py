# file .pcapng fornito, indizio: pacchetti HTTP
# Wireshark > Follow HTTP Stream al packet numero 2
# il nome del file suggerisce di guardare agli headers, dove c'è la flag in base64

import base64
 
# GET /CartellaPrivata/ HTTP/1.1
authorization_basic = "dXNlcjpJVEFTRUN7QV9iNHNpY19mbDRnX2Ywcl9hX2I0c2ljX2F1dGh9"
flag = base64.b64decode(authorization_basic)
print(flag)