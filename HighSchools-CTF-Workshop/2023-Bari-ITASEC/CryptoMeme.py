# Questo (non) è un esempio di scambio tra chiave e testo cifrato.
# CESARE: DECRIPTA QUESTO TESTO HJVMJVTWJHFOFSF E USALO COME CHIAVE
# VIGENERE: OK GRAZIE ECCO LA MIA FLAG OBUDMW{UCIJ_GNIJEX_JUDMX_TGIOWR}

def Cesare(testocifrato, shift):
	result = ''
	for c in testocifrato:
		if c.isalpha():
			base = ord('A') if c.isupper() else ord('a')
			result += chr((ord(c) - base - shift) % 26 + base)
		else:
			result += c
	return result

def Vigenere(testocifrato, chiave):
	testo = ''
	chiave = chiave.upper()
	lunghezza_chiave = len(chiave)
	indice_chiave = 0
	for c in testocifrato:
		if c.isalpha():
			base = ord('A') if c.isupper() else ord('a')
			k = ord(chiave[indice_chiave % lunghezza_chiave]) - ord('A')
			testo += chr((ord(c) - base - k) % 26 + base)
			indice_chiave += 1
		else:
			testo += c
	return testo

cesare = "HJVMJVTWJHFOFSF"
flag = "OBUDMW{UCIJ_GNIJEX_JUDMX_TGIOWR}"

for shift in range(1, 26):
	chiave = Cesare(cesare, shift)
	print(f"Shift {shift}: {chiave}")
	if chiave.isalpha():
		flag = Vigenere(flag, chiave)
		print(f"{flag}\n")
		
        # alla fine vedrai che è il primo shift a funzionare
