import requests

url = "http://web-02.challs.olicyber.it/server-records"
params = {"id": "flag"}
response = requests.get(url, params=params)
print("Status code:", response.status_code)
print(response.text)

# flag{wh47_i5_y0ur_qu3ry}