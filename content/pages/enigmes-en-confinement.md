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

<form onSubmit="return submitAnswer(this)" data-answer-pattern="Ym9iLitwb25nZQ==">
  <input type="text"></input>
  <input type="submit" value="?"></input>
  <div style="display: none" class="answer-correct">Bravo ! C'est la bonne réponse 👍 🎉 🤩</div>
  <div style="display: none" class="answer-wrong">Râté ! Essaie encore 😁</div>
</form>


<script>
function submitAnswer(form) {
  const answerPattern = atob(form.dataset.answerPattern);
  const answerRegex = new RegExp(answerPattern, 'i');
  const textInput = form.querySelector('input[type="text"]');
  const correctAnswerDiv = form.querySelector('.answer-correct');
  const wrongAnswerDiv = form.querySelector('.answer-wrong');
  if (answerRegex.test(textInput.value)) {
    wrongAnswerDiv.style.display = 'none';
    correctAnswerDiv.style.display = 'block';
  } else {
    correctAnswerDiv.style.display = 'none';
    wrongAnswerDiv.style.display = 'block';
  }
  return false;
}
</script>

<style>
article input[type="text"] {
  font-size: 3rem;
  width: 30rem;
}
article input[type="submit"] {
  font-size: 3rem;
  height: 5rem;
  width: 5rem;
  border-radius: 1rem;
  border: 0;
  background-color: #39b39d;
  color: white;
  cursor: pointer;
}
.answer-correct, .answer-wrong {
  font-size: 3rem;
  padding: 2rem;
}
</style>
