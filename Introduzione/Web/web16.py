import requests
from bs4 import BeautifulSoup
from collections import deque

url = 'http://web-16.challs.olicyber.it/'
queue, visited = deque([url]), set()

while queue:
    current = queue.popleft()
    if current in visited: continue
    visited.add(current)
    
    response = requests.get(current)
    print(f"Richiesta a {current}, Stato: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if (h1 := soup.find('h1')) and 'flag' in h1.text.lower():
        print(f"Flag trovata. Posizione: {current}:, Flag: {h1.text.strip()}")
        break
    
    for link in [a['href'] for a in soup.find_all('a', href=True)]:
        full_link = f'http://web-16.challs.olicyber.it{link}' if link.startswith('/') else link
        if full_link not in visited: queue.append(full_link)

# flag{5n00ping_4r0und}