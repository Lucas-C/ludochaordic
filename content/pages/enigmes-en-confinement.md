Title: Énigmes en confinement
Tags: lang:fr, enigme, jeux
Slug: enigmes-en-confinement
Status: hidden
---

En cette période de cocooning forcé, voici quelques énigmes pour faire travailler vos méninges !

<ul id="toc"></ul>

## 24 mars - Rébus Concept n°1

Si vous ne connaissez pas le jeu [Concept](https://concept-the-game.com),
les règles sont disponibles [ici (PDF 10,3Mo)](http://spelarch.vives.be/PDFspelregels/16056.pdf) pour déchiffrer cette énigme.
<!-- PDFs "officiels" en 2 parties :
  * https://concept-the-game.com/concept/files/rules/CONCEPT-RULES-FR.pdf
  * https://concept-the-game.com/concept/files/rules/CONCEPT-HELPSHEET-FR.pdf
-->

Qui suis-je ?

![](images/enigmes/enigme-concept-01.png)


### Teste ta réponse :

<form id="challenge-2020-03-24" data-min-score="50" data-hash="3820ea262dc61608e2ed700ab6d027404d55702a960dc6eed0155a37c7d94a82"></form>


## 25 mars - Rébus Concept n°2

Qui suis-je ?

![](images/enigmes/enigme-concept-03.png)

### Teste ta réponse :

<form id="challenge-2020-03-25" data-min-score="50" data-hash="8aaddb5664c898b76931eaf49db48aed6186ffefbd9138c8cce479140d86c762"></form>


## 26 mars - Énigmage n°1

De quel film suis-je le poster ?

Cliquez sur l'image pour en révéler petit à petit de plus en plus...

<img class="enigmage" src="images/enigmes/enigmage01-1.jpg">

### Teste ta réponse :

<form id="challenge-2020-03-26" data-hash="c01f23da736030c44c1927717ecdc5db1d06a33f5b5d0675d5e6c29cb693712e"></form>


## 27 mars - Énigmage n°2

Cliquez sur l'image pour en révéler petit à petit de plus en plus...

<img class="enigmage" src="images/enigmes/enigmage02-1.jpg">

### Teste ta réponse :

<form id="challenge-2020-03-27" data-hash="3bbdd5b84c61752f65efc0dd815b6c225cb8f013e9fcc3177b4e8637111b74cb"></form>


## 28 mars - Rébus Concept n°3

![](images/enigmes/enigme-concept-05.png)

### Teste ta réponse :

<form id="challenge-2020-03-28" data-hash="cdefd09a164e7b3e1c127ae3e8c22c02ef1be14a99725ed7040e77c1441d4d92"></form>


## 29 mars - Énigmage n°3

De quel film suis-je le poster ?

Cliquez sur l'image pour en révéler petit à petit de plus en plus...

<img class="enigmage" src="images/enigmes/enigmage03-1.jpg">

### Teste ta réponse :

<form id="challenge-2020-03-29" data-hash="8c2a25260209b2db50e9d7c369876ddeeaebde2472a38426ca4907fbe4135921"></form>


## 30 mars - Rébus Concept n°4

![](images/enigmes/enigme-concept-06.png)

### Teste ta réponse :

<form id="challenge-2020-03-30" data-hash="c212017ccdcd7bf803feb6188751f7c0afd902b2d42859ffd1a38129169e20c5"></form>


<!-- WIP
## ? avril - Esquissé

<div id="challenge-2020-04-31" class="esquisse"></div>
-->


## Scores

<table>
  <thead><tr> <th>Joueur</th> <th>Score</th> </tr></thead>
  <tbody id="highscores"></tbody>
</table>

- une réponse trouvée du premier coup donne **100 points**
- chaque tentative erronée fait perdre **10 points**
- pour les Rébus Concept, vous gagnez au minimum **50 points** si vous trouvez la réponse
- pour les Énigmages, chaque nouvelle zone révélée coûte **20 points**


<script src="https://www.gstatic.com/firebasejs/7.12.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/7.12.0/firebase-firestore.js"></script>
<script src="https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"></script>
<script>
firebase.initializeApp({
  apiKey: "AIzaSyBUA2secspKjZIA-_G3gCqcgYrlx5G94QE",
  authDomain: "scoreboard-7a578.firebaseapp.com",
  databaseURL: "https://scoreboard-7a578.firebaseio.com",
  projectId: "scoreboard-7a578",
  storageBucket: "scoreboard-7a578.appspot.com",
  messagingSenderId: "1085958736716",
  appId: "1:1085958736716:web:4c0ea416008a37c20edde9"
});
const scoreBoardCollec = firebase.firestore().collection('EnigmesDeConfinement');
const lockCollec = firebase.firestore().collection('Locks');
function updateScoreBoardTable() {
  const tbody = document.getElementById('highscores');
  while (tbody.firstChild) { tbody.removeChild(tbody.firstChild); }
  scoreBoardCollec.get().then(query => {
    const highScores = [];
    query.forEach(doc => highScores.push({
      playerName: doc.id,
      totalScore: Object.values(doc.data().scores).reduce((a, b) => a + b),
    }));
    highScores.sort((a, b) => b.totalScore - a.totalScore);
    highScores.forEach(highScore => tbody.appendChild(htmlTableRow([highScore.playerName, highScore.totalScore])))
  });
}
function htmlFromStr(string) {
  const div = document.createElement('div');
  div.innerHTML = string;
  return div.children[0];
}
function appendHtmlElemsFromStr(parent, string) {
  const div = document.createElement('div');
  div.innerHTML = string;
  while (div.children[0]) {
    parent.appendChild(div.children[0]);
  }
}
function insertAfter(existingNode, newNode) {
  existingNode.parentNode.insertBefore(newNode, existingNode.nextElementSibling);
}
function htmlTableRow(values) {
  const tr = document.createElement('tr');
  values.forEach(value => {
    const td = document.createElement('td');
    td.textContent = value;
    tr.appendChild(td);
  })
  return tr;
}
String.prototype.rsplit = function(sep, maxsplit) {
  const split = this.split(sep);
  return maxsplit ? [ split.slice(0, -maxsplit).join(sep) ].concat(split.slice(-maxsplit)) : split;
}
// Initialization:
const SLUG_CHAR_RANGE_TO_IGNORE = '[\x00-\x2F\x3A-\x40\x5B-\x60\x7B-\uFFFF]+';
window.malusPerChallenge = {}
window.submittedAnswer = {};  // Context to communicate between forms
const toc = document.getElementById('toc');
document.querySelectorAll('article h2').forEach(h2 => {
  h2.id = slugify(h2.textContent);
  toc.appendChild(htmlFromStr(`<li><a href="pages/enigmes-en-confinement.html#${h2.id}">${h2.textContent}</a></li>`));
});
document.querySelectorAll('article form').forEach(form => {
  form.onsubmit = submitConceptAnswer.bind(form);
  appendHtmlElemsFromStr(form, `<input type="text"></input>
                                <input type="submit" value="?"></input>
                                <div style="display: none" class="answer-correct">Bravo ! C'est la bonne réponse 👍 🎉 🤩</div>
                                <div style="display: none" class="answer-wrong">Râté ! Essaie encore 😁</div>`);
  insertAfter(form, htmlFromStr(`<form class="scoreForm" style="display: none" onSubmit="return submitPlayerScore(this)">
    <label for="playerName">Entre ton nom si tu souhaite apparaître dans les <a href="pages/enigmes-en-confinement.html#scores">scores</a> :</label>
    <input type="text" name="playerName" minlength="3"></input>
    <input type="submit" value="💯"></input>
    <div style="display: none" class="score-already-set">🚫 Vous avez déjà joué !</div>
    <div style="display: none" class="score-submitted">Score enregistré : <span class="score"></span> points</div>
  </form>`));
});
document.querySelectorAll('.enigmage').forEach(img => {
  imagesLoaded(img).on('done', preloadNextImg.bind(img));
  img.onclick = function () {
    const challengeId = this.parentElement.nextElementSibling.nextElementSibling.id;
    this.src = nextImage(this.src);
    window.malusPerChallenge[challengeId] = (window.malusPerChallenge[challengeId] || 0) + 20;
  }
});
function nextImage(imgSrc) {
  const [base, ext] = imgSrc.rsplit('.', 1);
  const [prefix, index] = base.split('-');
  return `${prefix}-${+index + 1}.${ext}`;
}
function preloadNextImg() {
  console.log('Preloaded:', this.src);
  const img = document.createElement('img')
  img.style.display = 'none';
  img.src = nextImage(this.src);
  imagesLoaded(img).on('done', preloadNextImg.bind(img));
  document.body.appendChild(img);
}
document.querySelectorAll('.esquisse').forEach(panel => {
  appendHtmlElemsFromStr(panel, `
    <form onSubmit="return submitDrawingGuess(this)">
      <canvas width="400" height="400"></canvas>
      <label for="drawingGuess">Que représente ce dessin ?</label>
      <input type="text" name="drawingGuess"></input>
      <input type="submit" value="👀"></input>
    </form>
    <form onSubmit="return submitDrawing(this)">
      <canvas width="400" height="400"></canvas>
      <label>Et maintenant dessine : "${panel.prevDrawingGuess}", puis clique ci-dessous</label>
      <input type="submit" value="👩‍🎨"></input>
    </form>
    <form class="overlay" onSubmit="return startEsquisse(this)">
      <h3>Esquissé !</h2>
      <label>Un seul joueur peut joueur à la fois.</label>
      <div class="lockFree">
        <label>Quand vous serez prêt, entrez votre nom et cliquez sur le bouton ci-dessous.</label>
        <label>Vous aurez 15min pour faire un tour du jeu <a href="https://www.jeux-goliath.com/produit/esquisse/">Esquissé</a></label>
        <input type="text" name="playerName" minlength="3"></input>
        <input type="submit" value="🎬"></input>
      </div>
      <div class="lockTaken" style="display: none">
        <label>Un joueur est en déjà train de jouer (<span class="lockPlayerName"></span>).</label>
        <label>Revenez un peu plus tard ! 😉</label>
      </div>
    </form>`);
  regularlyCheckEsquisseLock(panel);
  const drawingGuessCanvas = panel.getElementsByTagName('form')[0];
  const drawingCanvas = panel.getElementsByTagName('form')[1];
  drawingCanvas.prevX = -1;
  drawingCanvas.prevY = -1;
  drawingCanvas.addEventListener('mousemove', e => draw(drawingCanvas, e), false);
  drawingCanvas.addEventListener('mousedown', e => draw(drawingCanvas, e, true), false);
  drawingCanvas.addEventListener('mouseup', e => draw(drawingCanvas, e, false), false);
  drawingCanvas.addEventListener('mouseout', e => draw(drawingCanvas, e, false), false);
  // TODO: load image & panel.prevDrawingGuess from firebase
});
function regularlyCheckEsquisseLock(panel) {
  const overlay = panel.getElementsByClassName('overlay')[0];
  if (overlay.style.display !== 'none') {
    const lockFree = overlay.getElementsByClassName('lockFree')[0];
    const lockTaken = overlay.getElementsByClassName('lockTaken')[0];
    lockCollec.doc(panel.id).get().then(lock => {
      if (lock.exists && lock.data().playerName) {
        lockFree.style.display = 'none';
        lockTaken.style.display = 'block';
        overlay.getElementsByClassName('lockPlayerName')[0].textContent = lock.data().playerName;
      } else {
        lockFree.style.display = 'block';
        lockTaken.style.display = 'none';
      }
    });
  }
  setTimeout(regularlyCheckEsquisseLock, 1000, panel);
}
function startEsquisse(overlayForm) {
  const panel = overlayForm.parentNode;
  console.log('startEsquisse panel=', panel);
  console.log('startEsquisse panel.id=', panel.id);
  const playerName = overlayForm.querySelector('input[type="text"]').value.trim();
  lockCollec.doc(panel.id).set({playerName})
  overlayForm.style.display = 'none';
  // TODO: remove lock after 15min, from ANY client (=> we need to store lockStartTime)
  return false;
}
function submitDrawingGuess(form) {
  const panel = form.parentNode;
  const canvas = form.getElementsByTagName('canvas')[0];
  panel.drawingGuess = form.querySelector('input[type="text"]').value;
  return false;
}
function submitDrawing(form) {
  const panel = form.parentNode;
  const canvas = form.getElementsByTagName('canvas')[0];
  // TODO: save panel.drawingGuess & drawing + display success msg
  return false;
}
// TODO: pas rejouable + button CLEAR
function draw(canvas, e, newFlagValue) {
  if (typeof newFlagValue !== 'undefined') {
    canvas.isDrawing = newFlagValue;
  }
  if (canvas.isDrawing) {
    const clientRect = e.target.getBoundingClientRect();
    const currX = e.clientX - clientRect.left;
    const currY = e.clientY - clientRect.top;
    if (canvas.prevX > 0) {
      const ctx = canvas.getContext('2d');
      ctx.strokeStyle = 'black';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(canvas.prevX, canvas.prevY);
      ctx.lineTo(currX, currY);
      ctx.stroke();
      ctx.closePath();
    }
    canvas.prevX = currX;
    canvas.prevY = currY;
  } else {
    canvas.prevX = -1;
    canvas.prevY = -1;
  }
}
updateScoreBoardTable();

function submitConceptAnswer() {
  const form = this;
  const answer = form.querySelector('input[type="text"]').value;
  const correctAnswerDiv = form.querySelector('.answer-correct');
  const wrongAnswerDiv = form.querySelector('.answer-wrong');
  window.submittedAnswer.minScore = +(form.dataset.minScore || '0');
  window.submittedAnswer.challengeId = form.id;
  window.submittedAnswer.score = 0;
  correctAnswerDiv.style.display = 'none';
  const scoreForm = form.nextElementSibling;
  scoreForm.style.display = 'none';
  wrongAnswerDiv.style.display = 'none';
  digestMessage(slugify(answer)).then(hash => {
    if (hash === form.dataset.hash) {
      window.submittedAnswer.score = 100;
      setTimeout(() => {
        correctAnswerDiv.style.display = 'block';
        scoreForm.style.display = 'block';
      }, 500);
    } else {
      window.malusPerChallenge[form.id] = (window.malusPerChallenge[form.id] || 0) + 10;
      setTimeout(() => { wrongAnswerDiv.style.display = 'block'; }, 500);
    }
  });
  return false;
}
function submitPlayerScore(form) {
  const playerName = form.querySelector('input[type="text"]').value.trim();
  const scoreAlreadySetDiv = form.querySelector('.score-already-set');
  const scoreSubmitedDiv = form.querySelector('.score-submitted');
  scoreAlreadySetDiv.style.display = 'none';
  scoreSubmitedDiv.style.display = 'none';
  const playerDoc = scoreBoardCollec.doc(playerName);
  const challengeId = window.submittedAnswer.challengeId;
  playerDoc.get().then(doc => {
    if (doc.exists) {
      const scores = doc.data().scores;
      if (scores.hasOwnProperty(challengeId)) {
        scoreAlreadySetDiv.style.display = 'block';
      } else {
        scores[challengeId] = playerScore();
        playerDoc.update({scores}).then(() => {
          form.querySelector('.score').textContent = scores[challengeId];
          scoreSubmitedDiv.style.display = 'block';
          updateScoreBoardTable();
        });
      }
    } else {
      const scores = {};
      scores[challengeId] = playerScore();
      playerDoc.set({scores}).then(() => {
        form.querySelector('.score').textContent = scores[challengeId];
        scoreSubmitedDiv.style.display = 'block';
        updateScoreBoardTable();
      });
    }
  });
  return false;
}
function playerScore() {
  const submittedAnswer = window.submittedAnswer;
  const challengeId = window.submittedAnswer.challengeId;
  const malus = window.malusPerChallenge[challengeId] || 0;
  return Math.max(submittedAnswer.minScore, submittedAnswer.score - malus);
}
function slugify(s) {
  s = String(s).trim().toLowerCase()
  s = s.normalize('NFD') 				 // separate accent from letter
  s = s.replace(/[\u0300-\u036f]/g, '')  // remove all separated accents
  s = s.replace(new RegExp('^'+SLUG_CHAR_RANGE_TO_IGNORE, 'g'), '')
  s = s.replace(new RegExp(SLUG_CHAR_RANGE_TO_IGNORE, 'g'), '-')
  s = s.replace(/^la-/g, '').replace(/^le-/g, '').replace(/-st-/g, '-saint-')
  s = s.replace(/^commandant-/g, '').replace(/^jacques-/g, '').replace(/^yves-/g, '')
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
article label {
  display: block;
  margin: 1rem 0;
}
article input[type="submit"] {
  border-radius: 1rem;
  border: 0;
  background-color: #39b39d;
  color: white;
  cursor: pointer;
  margin: 0 .5rem;
}
@media screen and (min-width: 40rem) {
  article label { font-size: 1.5rem; }
  article input[type="text"] {
    font-size: 2.5rem;
    width: 22rem;
  }
  article input[type="submit"] {
    font-size: 2.5rem;
    height: 5rem;
    width: 5rem;
  }
  .answer-correct, .answer-wrong {
    font-size: 2.5rem;
    padding: 2rem;
  }
  .scoreForm { padding-left: 2rem; }
  .score-already-set, .score-submitted {
    font-size: 1.25rem;
    padding: 1rem;
  }
}
article table {
  border-spacing: 0;
  border-collapse: collapse;
  font-size: 1.2rem;
  margin: 0 auto;
  margin-bottom: 4rem;
}
article td, article th {
  padding: 1rem;
  border-top: 1px solid #ddd;
}
article th {
  border-bottom: 2px solid #ddd;
  border-top: 0;
}
article tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.enigmage {
  max-height: 60rem;
  cursor: pointer;
}
.esquisse {
  position: relative;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
.overlay {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: black;
  opacity: .75;
  border-radius: 1rem;
  display: flex;
  flex-flow: column;
  align-items: center;
  text-align: center;
  color: white;
}
.overlay h3 {
  font-size: 3rem;
  color: white;
  margin: 4rem;
}
.overlay label {
  font-size: 2rem;
  max-width: max-content !important;
  line-height: 2rem;
  margin: 2rem;
}
.esquisse canvas {
  border: 1px solid black;
  cursor: pointer;
  margin: .5rem 0;
}
.esquisse label { max-width: 400px; }
</style>
