# Questo sito ti permette di scaricare la flag, è solo un po' lento...

import requests

url = 'http://flagdownloader.challs.olicyber.it/'

# il file che contiene la flag è quello che si chiama "Sicuramente non la flag"
# puoi avere piano premium o piano gratuito, che viene appositamente rallentato da una chiamata a setTImeout
# io per risolverla, ho modificato il source code JS dai devtools e ho impostato a 0 il delay del timeout

# qui ho automatizzato il processo che effettua direttamente le richieste al server per avere i blocchi
result = []
next_block = '0'
while next_block:
    response = requests.get(f"{url}/download/flag/{next_block}")
    data = response.json()
    next_block = data['n']
    result.append(data['c'])
print(''.join(result))