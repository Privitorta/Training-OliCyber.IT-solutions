import requests

# curl -I http://staticwebfoundation.challs.olicyber.it/
# dava un curioso:
'''Refresh: 86400; url=/o1SfuSXpptIk1p8U0qISobkrYwXSILflr6ZxTsmF?p=banana'''
# dunque...

url = "http://staticwebfoundation.challs.olicyber.it/o1SfuSXpptIk1p8U0qISobkrYwXSILflr6ZxTsmF"
parolamagica = ["banana"]

for p in parolamagica:
    r = requests.get(url, params={"p": p})
    contenuto = r.text.strip()
    if "ptm{" in contenuto:
        print(contenuto)
        break