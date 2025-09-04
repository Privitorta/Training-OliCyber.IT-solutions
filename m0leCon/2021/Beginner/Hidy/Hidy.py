# I got a hold of this TOP-SECRET document but it seems to be redacted.
# Can you read all the intel?

import re

priviregex = r'<span class="(redacted)">(.)</span>'
priviregex2 = r'\[(\d*?)\]\.remove\(\);'
try:
	with open('redacted.html', 'r', encoding='utf-8') as f:
		text = f.read()
except FileNotFoundError:
	print("File 'redacted.html' non trovato. Assicurati che sia nella stessa cartella dello script.")
	exit(1)
spans = [x[1] for x in re.findall(priviregex, text)]
print('ptm{' + ''.join(spans) + '}')