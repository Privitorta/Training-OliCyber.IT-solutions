# In Python, lo xor tra due numeri interi è dato dall'operatore ^. 
# Per fare lo xor tra due stringhe, è necessario convertirle dapprima in bytes, 
# per poi effettuare l'operazione byte per byte.

# Per ottenere la flag di questa challenge, effettua lo xor di questi due messaggi: 
# fai attenzione a decodificare correttamente da esadecimale a bytes!

privi1 = bytes.fromhex("158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf")
privi2 = bytes.fromhex("73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2")
print(bytes(a ^ b for a, b in zip(privi1, privi2)).decode())

# metodo: One Time Pad (OTP)