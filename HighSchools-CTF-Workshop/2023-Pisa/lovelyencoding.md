> Javascript is awesome (no, it's not!) 

Il sito si apre con una encoded flag: `synt{jnvg_vf_guvf_pelcgb_be_jro}`. Ma nel source code c'è uno script JS che estraiamo:

```javascript
document.getElementById("myForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const inputText = document.getElementById("inputText").value;
  const encoded_flag = "synt{jnvg_vf_guvf_pelcgb_be_jro}";
  check_value(encoded_flag, inputText);
});

function customEncode(inputString, shift) {
  if (typeof inputString !== "string" || typeof shift !== "number") {
    throw new Error("Input must be a string, and shift must be a number");
  }

  let encodedString = "";

  for (let i = 0; i < inputString.length; i++) {
    const char = inputString.charAt(i);
    const charCode = inputString.charCodeAt(i);

    if (/[a-zA-Z]/.test(char)) {
      const isUpperCase = char === char.toUpperCase();
      const baseCharCode = isUpperCase ? "A".charCodeAt(0) : "a".charCodeAt(0);
      const shiftedCharCode =
        ((((charCode - baseCharCode + shift) % 26) + 26) % 26) + baseCharCode;
      encodedString += String.fromCharCode(shiftedCharCode);
    } else {
      encodedString += char;
    }
  }

  return encodedString;
}

function customDecode(encodedString, shift) {
  return customEncode(encodedString, -shift);
}

function check_value(encodedString, plaintext) {
  if (encodedString === customEncode(plaintext, 13)) {
    document.getElementById("success").innerHTML =
      "Winner winner chicken dinner!!!";
  }
}
```

La flag è codificata con **rot13** (uno shift di 13 lettere, comune nelle CTF). Nel JS c'è una funzione *customEncode* che viene usata per la cifratura della flag, ma è presente anche la funzione **customDecode**; chiamare tale funzione da console browser passando come input la flag criptata e lo shift 13 riceviamo la flag finale. Il comando è proprio:

```javascript
customDecode("synt{jnvg_vf_guvf_pelcgb_be_jro}", 13)
```