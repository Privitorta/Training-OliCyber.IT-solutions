from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import pad, unpad

def main():
	print("Scegli algoritmo: DES, AES, ChaCha20")
	algo = input("Algoritmo: ").strip().upper()
	op = input("Operazione (encrypt/decrypt): ").strip().lower()
	key_hex = input("Chiave (hex): ").strip()
	key = bytes.fromhex(key_hex)

	if algo == "DES":
		mode = input("Modalità (CBC): ").strip().upper() or "CBC"
		iv_hex = input("IV (hex, 8 byte): ").strip()
		iv = bytes.fromhex(iv_hex)
		if op == "encrypt":
			pt = input("Plaintext: ").encode()
			padding = input("Padding (x923/pkcs7/none): ").strip().lower() or "x923"
			if padding == "none":
				padded = pt
			else:
				padded = pad(pt, 8, padding)
			cipher = DES.new(key, DES.MODE_CBC, iv=iv)
			ct = cipher.encrypt(padded)
			print("Ciphertext (hex):", ct.hex())
		else:
			ct = bytes.fromhex(input("Ciphertext (hex): ").strip())
			cipher = DES.new(key, DES.MODE_CBC, iv=iv)
			pt = cipher.decrypt(ct)
			try:
				padding = input("Padding (x923/pkcs7/none): ").strip().lower() or "x923"
				if padding == "none":
					print("Plaintext:", pt.decode())
				else:
					print("Plaintext:", unpad(pt, 8, padding).decode())
			except Exception as e:
				print("Plaintext (raw):", pt)

	elif algo == "AES":
		mode = input("Modalità (CFB/CBC): ").strip().upper() or "CFB"
		iv_hex = input("IV (hex, 16 byte, vuoto=auto): ").strip()
		iv = bytes.fromhex(iv_hex) if iv_hex else None
		segment_size = 128
		if mode == "CFB":
			try:
				segment_size = int(input("Segment size (default 128): ") or 128)
			except:
				segment_size = 128
		if op == "encrypt":
			pt = input("Plaintext: ").encode()
			padding = input("Padding (pkcs7/none): ").strip().lower() or "pkcs7"
			if padding == "none":
				padded = pt
			else:
				padded = pad(pt, 16, padding)
			if mode == "CFB":
				cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=segment_size) if iv else AES.new(key, AES.MODE_CFB, segment_size=segment_size)
			else:
				cipher = AES.new(key, AES.MODE_CBC, iv=iv) if iv else AES.new(key, AES.MODE_CBC)
			ct = cipher.encrypt(padded)
			print("Ciphertext (hex):", ct.hex())
			print("IV usato:", cipher.iv.hex())
		else:
			ct = bytes.fromhex(input("Ciphertext (hex): ").strip())
			if mode == "CFB":
				cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=segment_size)
			else:
				cipher = AES.new(key, AES.MODE_CBC, iv=iv)
			pt = cipher.decrypt(ct)
			try:
				padding = input("Padding (pkcs7/none): ").strip().lower() or "pkcs7"
				if padding == "none":
					print("Plaintext:", pt.decode())
				else:
					print("Plaintext:", unpad(pt, 16, padding).decode())
			except Exception as e:
				print("Plaintext (raw):", pt)

	elif algo == "CHACHA20":
		nonce_hex = input("Nonce (hex, 8 byte): ").strip()
		nonce = bytes.fromhex(nonce_hex)
		if op == "encrypt":
			pt = input("Plaintext: ").encode()
			cipher = ChaCha20.new(key=key, nonce=nonce)
			ct = cipher.encrypt(pt)
			print("Ciphertext (hex):", ct.hex())
		else:
			ct = bytes.fromhex(input("Ciphertext (hex): ").strip())
			cipher = ChaCha20.new(key=key, nonce=nonce)
			pt = cipher.decrypt(ct)
			try:
				print("Plaintext:", pt.decode())
			except:
				print("Plaintext (raw):", pt)
	else:
		print("Algoritmo non supportato.")

if __name__ == "__main__":
	main()