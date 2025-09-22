import requests
from bs4 import BeautifulSoup, Comment

url = "http://web-14.challs.olicyber.it/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for c in comments:
    print(c)
    c.extract()

# flag{50m3b0dy_f0rg07_70_d31373_7hi5} 