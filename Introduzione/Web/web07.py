import requests

url = "http://web-07.challs.olicyber.it/"
response = requests.head(url)
print(response.headers)

# flag{r0gu3_m374d474}