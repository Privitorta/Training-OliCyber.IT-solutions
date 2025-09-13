> C'è un file nascosto che potrebbe contenere una flag, riuscirai a trovarlo? :^)

Viene citato un file nascosto. Generalmente, quando si parla di file, il primo capro espiatorio che si prova è il file robots.txt, un file di testo che viene usato frequentemente per gestire il traffico dei [Crawler](https://it.wikipedia.org/wiki/Crawler) (web crawler) verso il sito.

Visitando /robots.txt all'URL dato, il risultato è:
```
User-agent: human-being
Allow: /
Disallow: /39185d1b78d1cec390b777d9e82c01a3/a35f6c043cd0f215ab114bc7824e25e1.gif
Disallow: /39185d1b78d1cec390b777d9e82c01a3/79df7045bba0bcb6303752558412f300.txt
```

Il primo percorso porta ad una GIF di Dario Moccia che dice DEH PEFFORZA DEH PEFFORZA DEH PEFFORZA invece il secondo file porta alla flag:

**flag{well_not_really_a_security_challenge_but_somewhere_you_need_to_start!}**