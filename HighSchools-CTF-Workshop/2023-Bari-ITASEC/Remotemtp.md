> Sono riuscito a fare RCE su questo servizio web, ho trovato un applicazione che permette di ricavare in parte il contenuro dei messaggi cifrati con il Many Time Pad, puoi aiutarmi a trovare il contenuto completo?

Qui bisogna andare un po' a logica e modificare anzitutto la riga 6, dove c'è la flag (ITASEC) completando gli spazi. Poi, modificare il resto e vedere come si formano parole e frasi, finchè non si ha la flag completa:

**ITASEC{Curv3B4ll_CVE-2020-0601}**