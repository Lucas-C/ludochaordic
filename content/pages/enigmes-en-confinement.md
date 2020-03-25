Title: Énigmes en confinement
Tags: lang:fr, enigme, jeux
Slug: enigmes-en-confinement
Status: hidden
---

En cette période de cocooning forcé, voici quelques énigmes pour faire travailler vos méninges !

## 24 mars - Rébus Concept n°1

Si vous ne connaissez pas le jeu [Concept](https://concept-the-game.com),
les règles sont disponibles [ici (PDF 10,3Mo)](http://spelarch.vives.be/PDFspelregels/16056.pdf) pour déchiffrer cette énigme.

Qui suis-je ?

![](images/enigmes/enigme-concept-01.png)


### Teste ta réponse :

<form onSubmit="return submitConceptAnswer(this)" data-hash="3820ea262dc61608e2ed700ab6d027404d55702a960dc6eed0155a37c7d94a82">
  <input type="text"></input>
  <input type="submit" value="?"></input>
  <div style="display: none" class="answer-correct">Bravo ! C'est la bonne réponse 👍 🎉 🤩</div>
  <div style="display: none" class="answer-wrong">Râté ! Essaie encore 😁</div>
</form>


## 25 mars - Rébus Concept n°2

Qui suis-je ?

![](images/enigmes/enigme-concept-03.png)

### Teste ta réponse :

<form onSubmit="return submitConceptAnswer(this)" data-hash="8aaddb5664c898b76931eaf49db48aed6186ffefbd9138c8cce479140d86c762">
  <input type="text"></input>
  <input type="submit" value="?"></input>
  <div style="display: none" class="answer-correct">Bravo ! C'est la bonne réponse 👍 🎉 🤩</div>
  <div style="display: none" class="answer-wrong">Râté ! Essaie encore 😁</div>
</form>


<script>
function submitConceptAnswer(form) {
  const textInput = form.querySelector('input[type="text"]');
  const correctAnswerDiv = form.querySelector('.answer-correct');
  const wrongAnswerDiv = form.querySelector('.answer-wrong');
  digestMessage(slugify(textInput.value)).then(hash => {
    if (hash === form.dataset.hash) {
      wrongAnswerDiv.style.display = 'none';
      correctAnswerDiv.style.display = 'block';
    } else {
      correctAnswerDiv.style.display = 'none';
      wrongAnswerDiv.style.display = 'block';
    }
  });
  return false;
}
const SLUG_CHAR_RANGE_TO_IGNORE = '[\x00-\x2F\x3A-\x40\x5B-\x60\x7B-\uFFFF]+';
function slugify(s) {
  s = String(s).trim().toLowerCase()
  s = s.normalize('NFD') 				 // separate accent from letter
  s = s.replace(/[\u0300-\u036f]/g, '')  // remove all separated accents
  s = s.replace(new RegExp('^'+SLUG_CHAR_RANGE_TO_IGNORE, 'g'), '')
  s = s.replace(new RegExp(SLUG_CHAR_RANGE_TO_IGNORE, 'g'), '-')
  return encodeURIComponent(s);
}
// FROM: https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest#Converting_a_digest_to_a_hex_string
async function digestMessage(message) {
  const msgUint8 = new TextEncoder().encode(message);                           // encode as (utf-8) Uint8Array
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);           // hash the message
  const hashArray = Array.from(new Uint8Array(hashBuffer));                     // convert buffer to byte array
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join(''); // convert bytes to hex string
  return hashHex;
}
//digestMessage(slugify("SOLUTION")).then(hash => console.log(hash));
</script>

<style>
article h2 { margin-top: 5rem; }
article input[type="submit"] {
  border-radius: 1rem;
  border: 0;
  background-color: #39b39d;
  color: white;
  cursor: pointer;
}
@media screen and (min-width: 40rem) {
  article input[type="text"] {
    font-size: 3rem;
    width: 30rem;
  }
  article input[type="submit"] {
    font-size: 3rem;
    height: 5rem;
    width: 5rem;
  }
  .answer-correct, .answer-wrong {
    font-size: 3rem;
    padding: 2rem;
  }
}
</style>
