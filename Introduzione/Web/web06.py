import requests

session = requests.Session()
response_token = session.get("http://web-06.challs.olicyber.it/token")
response_flag = session.get("http://web-06.challs.olicyber.it/flag")
print(response_flag.text)

# flag{7w0_574g3_4cc3s5}