# Sei in grado di trovare i robots?

import requests
import re

url = "http://no-robots.challs.olicyber.it/"

robots_url = url + "robots.txt"
robots_txt = requests.get(robots_url).text
print("Contenuto:\n", robots_txt)
paths = re.findall(r"Disallow: (/.+)", robots_txt)
if paths:
	for path in paths:
		print("\nPercorso trovato:", path)
		hidden_url = url + path.lstrip("/")
		response = requests.get(hidden_url)
		print(f"\nContenuto '{hidden_url}':\n", response.text)
		flag_match = re.search(r'flag\{[^}]+\}', response.text, re.IGNORECASE)
		if flag_match:
			print("Flag:", flag_match.group(0))
else:
	print("Loser")

