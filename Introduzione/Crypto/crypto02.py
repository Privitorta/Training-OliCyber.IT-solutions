# Convenzionalmente le sequenze di bit vengono divise in byte: sottosequenze adiacenti di 8 bit ciascuna.
# La codifica esadecimale (o in base 16) permette di rappresentarli in modo molto conveniente.
# Dato un byte, lo si spezza in due sequenze adiacenti da quattro bit ciascuna: queste, 
# lette in binario, possono essere intese come due numeri interi da 0 a 15, 
# che sono poi rappresentati dai caratteri '0', '1', ..., '9', 'a', 'b', ..., 'f'.
# Esempio: 01101110 → 0110, 1110 → 6, 14 → '6', 'e' → '6e'.
# Dunque ciascun byte viene trasformato in una sequenza di due caratteri.

# In Python, sequenze di byte vengono gestite attraverso la classe bytes. Con il metodo .hex() è possibile ottenere la corrispondente stringa esadecimale, mentre la funzione bytes.fromhex(s) restituisce l'oggetto bytes che corrisponde alla stringa esadecimale s.
# Per ottenere la flag, trasforma la seguente stringa nella corrispondente sequenza di bytes.
# 666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d

print(bytes.fromhex("666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d").decode())