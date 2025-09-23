# Il futuro è già qua: prova il nostro sistema rivoluzionario!

from pwn import remote

# funzione per connettersi al server e estrarre i bit della flag
def priviExtract(num_bits=400): # numero di bit da estrarre
    with remote('chooseyourotp.challs.olicyber.it', 38302) as s:
        bits = 0
        for i in range(num_bits): # estrai bit per bit
            prompt = s.recvuntil('> ')
            print(f"Received prompt for bit {i}") # Debug: mostra il prompt ricevuto
            s.sendline(f"{1 << i}") 
            response = int(s.recvline())
            bit = (response >> i) & 1
            bits |= (bit << i)
        return bits, num_bits

def priviConvert(bits):
    bit_str = bin(bits)[2:] # converti in stringa binaria senza '0b'
    if len(bit_str) % 8 != 0:
        bit_str = bit_str.zfill((len(bit_str) + 7) // 8 * 8) # serve ad aggiungere zeri a sinistra se non è multiplo di 8
    flag_bytes = int(bit_str, 2).to_bytes(len(bit_str) // 8, byteorder='big') # converto in bytes
    try: 
        return flag_bytes.decode() # prova a decodificare in stringa
    except Exception:
        return flag_bytes

if __name__ == "__main__":
    bits, n = priviExtract()
    flag = priviConvert(bits, n)
    print(flag)