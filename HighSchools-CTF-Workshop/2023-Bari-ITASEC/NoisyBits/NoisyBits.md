Viene dato un file bitmap con un immagine disturbata, appunto, come suggerisce il titolo della challenge.

![](/HighSchools-CTF-Workshop/2023-Bari-ITASEC/NoisyBits/bits.bmp)

I colori bianco e nero sono gli unici della foto, quindi il primo pensiero che giunge, è che siano in realtà bit posti a 0 o 1 di un file; per recuperarlo, bisogna prendere tutti i valori rappresentati dai pixel, convertirli in una stringa binaria e convertire infine quest'ultima in byte.

Runnare uno script python (allegato) aiuta a recuperare il file in questione:
```python
from PIL import Image

def main():
    filename = "bits.bmp"
    raw = Image.open(open(filename, "rb")).tobytes()
    bin_str = bytes([(x&1)+48 for x in raw]).decode()
    decoded = bytes(int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8))
    with open("output", "wb") as f:
        f.write(decoded)
    print("Output scritto in 'output'")
if __name__ == "__main__":
    main()
```
Ora che abbiamo il file di output, si può vedere il tipo di file con:
```bash
file output
output: Zip archive data, at least v2.0 to extract, compression method=deflate
```
Che ci darà un file con la flag visibile con:
```bash
cat flag.txt
```