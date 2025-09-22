# In Python per convertire un oggetto bytes in un oggetto int è conveniente utilizzare 
# la funzione int.from_bytes(b, endianness), ove b è il nostro oggetto bytes, 
# mentre endianness è una stringa 'big' oppure 'little' che sta ad indicare 
# in che ordine devono essere letti i byte di b: rispettivamente da sinistra verso destra e viceversa.
# Per convertire un intero z in bytes puoi usare invece la funzione (z).to_bytes(n, endianness): 
# n indica il numero di bytes da utilizzare per la conversione, seguendo l'ordine dato da endianness.

# La flag di questa challenge è spezzata in due metà: decodifica la prima parte da base64, 
# mentre per la seconda parte converti il numero dato (in base10) a bytes, in big endian.

# ZmxhZ3t3NDF0XzF0c19hbGxfYjE=
# 664813035583918006462745898431981286737635929725

import base64
print(base64.b64decode("ZmxhZ3t3NDF0XzF0c19hbGxfYjE=").decode() + bytes.fromhex(hex(664813035583918006462745898431981286737635929725)[2:]).decode())