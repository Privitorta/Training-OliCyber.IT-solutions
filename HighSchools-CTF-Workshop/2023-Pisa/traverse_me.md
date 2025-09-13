> Ho trovato questa galleria di quadri, chissà se ce ne sono di nascosti. 
> La flag è in /flag.txt

Il sito si apre su una galleria di 3 foto che si possono scorrere e aprire singolarmente. All'apertura di una delle foto, l'URL è strutturato così: `http://traverse.challs.olicyber.it/serve_file?filename=painting1.png`. L'endpoint `/serve_file` rende possibile visualizzare singolarmente le immagini mostrate e accetta come query parameter "filename", che contiene il nome dell'immagine desiderata. Nell'accesso alle foto c'è una **path traversal** quindi fornendo come filename la stringa `../../../flag.txt` possiamo accedere al file della flag situato nella root folder:

```
http://traverse.challs.olicyber.it/serve_file?filename=../../../flag.txt
```

**flag{m3_and_7h3_boys_a77rav3rsando1a}**