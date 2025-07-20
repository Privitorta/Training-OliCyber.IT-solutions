'''
; <<>> DiG 9.18.30-0ubuntu0.24.04.2-Ubuntu <<>> -t txt -p10500 @pisani.challs.olicyber.it 00000000-0000-4000-0000-000000000000.maze.localhost
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59369
;; flags: qr rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;00000000-0000-4000-0000-000000000000.maze.localhost. IN        TXT

;; ANSWER SECTION:
00000000-0000-4000-0000-000000000000.maze.localhost. 3600 IN TXT "Navigate:" "up.00000000-0000-4000-0000-000000000000.maze.localhost." "right.00000000-0000-4000-0000-000000000000.maze.localhost." "down.00000000-0000-4000-0000-000000000000.maze.localhost." "left.00000000-0000-4000-0000-000000000000.maze.localhost."

;; Query time: 64 msec
;; SERVER: 5.75.221.48#10500(pisani.challs.olicyber.it) (UDP)
;; WHEN: Sun Jul 20 22:59:01 CEST 2025
;; MSG SIZE  rcvd: 373 
'''

# sta dicendo che dal nodo "00000000-..." posso muovermi in quattro direzioni (up, right, down, left) 
# e ogni direzione è un nuovo hostname su cui fare la query successiva

''' hint 1: Todo el mundo Una mano en la cabeza Una mano sul.... muro? '''
# la regola della mano destra per un labirinto funziona che metti la mano destra su un muro e segui quel muro
# dunque accade che ad ogni passo controlli la direzione alla tua destra, poi avanti, poi sinistra, poi indietro, per decidere dove andare
''' hint 2: "Wall Follower: right-hand rule", a meno che tu non sia mancino, in quel caso "left-hand rule". '''
# in termini di labirinto testuale:
# parti da una posizione iniziale e una direzione (es. "up"). 
# ad ogni nodo, scegli il prossimo passo secondo questa priorità: 
    # vai a destra rispetto alla direzione corrente, se possibile. 
    # altrimenti, vai avanti.
    # altrimenti, vai a sinistra.
    # altrimenti, torna indietro.

import dns.resolver
import socket