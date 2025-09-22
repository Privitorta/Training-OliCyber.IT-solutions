import requests
from bs4 import BeautifulSoup

url = 'http://web-12.challs.olicyber.it/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

paragrafi = soup.find_all('p')
print(paragrafi)

# flag{7h3_14ngu4g3_0f_7h3_w3b}