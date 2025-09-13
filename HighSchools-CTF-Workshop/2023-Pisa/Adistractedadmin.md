> Sembra che sia riuscito ad intercettare la password dell'admin mentre accedeva al suo sito, puoi aiutarmi a ritrovarla?

Dal file .pcapng, filtro le richieste HTTP. Una ben poco nascosta GET /admin.php mi porta in fretta alle credenziali dell'admin in una descrizione:

**Credentials: admin:flag{un4_p4ssw0rd_veram3nte_n4sc0sta}**