Dato che per questa challenge che ha avuto originariamente 0 solve ci sono 3 soluzioni possibili di cui una intended, vediamole nel dettaglio tutte.

### Soluzione 1
Consideriamo la funzione di verifica: una firma $(s_1, s_2)$ è valia se

$$
s_2^e \equiv h(u)s_1^{h(m)} \pmod{n}
$$

dove $u$ è il nome utente, $m$ è il messaggio e $h$ è la funzione hash `sha256`. Dato che non ci importa come viene generata la firma lo ignoreremo; supponiamo di ottenere una firma $(s_1, s_2)$ per il messaggio `ACK` dall'admin. Utilizzando l'algoritmo dell'MCD esteso possiamo trovare due coefficienti $a$ e $b$ tali che

$$
a\cdot e - b\cdot h(m_t) = -h(m_a)
$$

dove $m_t$ è il messaggio che vogliamo firmare e $m_a$ è semplicemente `ACK`. Calcoliamo $s_1' = s_1^e$ e $s_2'=s_2s_1^a$. Questa coppia è una firma valida per $m_t$ perchè la verifica si riduce a quella per $m_a$.

### Soluzione 2
Per questa solve serve sapere come viene creata la firma; essa, dato un messaggio $m$ e un utente $u$ prende un numero casuale $r$ e si calcola $(s_1, s_2) = (r^e, h(u)^d\cdot r^{h(m)})$, con $d$ esponente privato della chiave RSA.

Se otteniamo una firma per un utente $u$ diverso da `admin` e un qualsiasi messaggio $m$ tale che $h(m) sia multiplo di $e$, possiamo avere il valore di $h(u)^d$ calcolando

$$
s_2\cdot s_1^{\frac{h(m)}{e}} \pmod{n}.
$$

Sia $u$ un utente per cui abbiamo recuperato $h(u)^d$ come spiegato nel passaggio precedente. Possiamo ora utilizzare la terza query per recuperare un random $r$ utilizzato per la firma di `ACK`. Sia $(s_1, s_2) = (r^e, h(u)^d\cdot r^{h(m_a)})$. Poiché conosciamo $h(u)^d$, possiamo recuperare il valore di $r^{h(m_a)}$. Poiché $\gcd(e, h(m_a)) = 1$, utilizzando l'identità di Bézout possiamo trovare $a, b$ tali che $a\cdot e + b\cdot h(m_a) = 1$. Possiamo quindi calcolare

$$
(r^e)^a \cdot (r^{h(m_a)})^b \pmod{n} = r^{a\cdot e + b\cdot h(m_a)} = r \pmod{n} = r,
$$

poiché $r < n$.

Poichè $r$ è generato con il modulo `random` di Python (Mersenne Twister), se ne osserviamo abbastanza possiamo ricostruire lo stato interno e prevedere i successivi valori di $r$; conoscendo i valori di $r$ utilizzati nella query 3, possiamo semplicemente inviare un messaggio a `admin` e recuperare $h(u_a)^d$ (l'utente admin) dividendo $s_2$ per $r^{h(m_a)}$ (cosa possibile poiché conosciamo $r$).

Ora otteniamo una firma per il messaggio $m_t$ selezionando un valore casuale $r$ e restituendo

$$
(s_1, s_2) = (r^e, h(u_a)^d\cdot r^{h(m_t)}).
$$

Verifichiamo la firma e abbiamo la flag.

### Soluzione 3

Sfruttando il fatto che siamo a conoscenza del nome utente `admin`, troviamo $a$ e $b$ tali che

$$
a\cdot h(m_t)+1 = e\cdot b
$$

Ponendo $s_1 = h(u_a)^a \pmod{n}$ e $s_2 = h(u_a)^b \pmod{n}$ otteniamo una firma valida.