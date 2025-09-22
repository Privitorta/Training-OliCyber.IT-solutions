import requests

url = "http://web-10.challs.olicyber.it/"
response = requests.options(url)
print(response.headers)
response = requests.put(url)
print(response.headers)

# flag{br34king_7h3_ru135}