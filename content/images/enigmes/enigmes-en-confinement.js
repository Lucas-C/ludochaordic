const ESQUISSE_GAME_TIME_IN_MINS = 10;
const SLUG_CHAR_RANGE_TO_IGNORE = '[\x00-\x2F\x3A-\x40\x5B-\x60\x7B-\uFFFF]+';

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
const esquissesCollec = firebase.firestore().collection('Esquisses');
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
    td.innerHTML = value;
    tr.appendChild(td);
  })
  return tr;
}
String.prototype.rsplit = function(sep, maxsplit) {
  const split = this.split(sep);
  return maxsplit ? [ split.slice(0, -maxsplit).join(sep) ].concat(split.slice(-maxsplit)) : split;
}
// Initialization:
window.malusPerChallenge = {}
window.submittedAnswer = {};  // Context to communicate between forms
const toc = document.getElementById('toc');
if (toc) {
  document.querySelectorAll('article h2').forEach(h2 => {
    h2.id = slugify(h2.textContent);
    toc.appendChild(htmlFromStr(`<li><a href="pages/enigmes-en-confinement.html#${h2.id}">${h2.textContent}</a></li>`));
  });
}
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
    const form = this.parentElement.nextElementSibling.nextElementSibling;
    const challengeId = form.id;
    this.src = nextImage(this.src);
    if (img.dataset.aprilJoke && this.src.endsWith('-7.jpg')) {
      const wrongAnswerDiv = form.querySelector('.answer-wrong');
      wrongAnswerDiv.style.display = 'none';
      const correctAnswerDiv = form.querySelector('.answer-correct');
      correctAnswerDiv.style.display = 'block';
      correctAnswerDiv.textContent = "Poisson d'avril !";
      window.malusPerChallenge[challengeId] = 0;
      const scoreForm = form.nextElementSibling;
      scoreForm.style.display = 'block';
      img.onclick = () => {};
    } else {
      window.malusPerChallenge[challengeId] = (window.malusPerChallenge[challengeId] || 0) + 20;
    }
  }
});
function nextImage(imgSrc) {
  const [base, ext] = imgSrc.rsplit('.', 1);
  const [prefix, index] = base.split('-');
  return `${prefix}-${+index + 1}.${ext}`;
}
function preloadNextImg() {
  const prevImg = this;
  console.log('Loaded:', prevImg.src);
  setTimeout(() => {
    const img = document.createElement('img')
    img.style.display = 'none';
    img.src = nextImage(prevImg.src);
    imagesLoaded(img).on('done', preloadNextImg.bind(img));
    document.body.appendChild(img);
  }, 500);
}
document.querySelectorAll('.esquisse').forEach(esquisse => {
  appendHtmlElemsFromStr(esquisse, `
    <form class="panels" onSubmit="return submitDrawingAndGuess(this)">
      <div class="panel">
        <canvas width="400" height="400"></canvas>
        <label for="guess">Un joueur précédent a dessiné ceci. Que vois-tu ?</label>
        <input type="text" name="guess" minlength="3"></input>
      </div>
      <div class="panel">
        <canvas width="400" height="400"></canvas>
        <label>Dessine ici : "<span class="drawingTitle"></span>"</label>
        <label>Pour tout effacer, clique ici : <button title="Tout effacer" onclick="clearDrawing(this)">🧹</button></label>
      </div>
      <div class="submission-panel">
        <label for="submitButton">Quand tu as fini les 2 parties du jeu, clique sur ce bouton :</label>
        <input type="submit" name="submitButton" value="👩‍🎨"></input>
        <div class="drawing-guess-submitted" style="display: none">
          <label>Bravo ! Magnifique !</label>
          <label>Le résultat de ce jeu collectif sera disponible dans quelques jours 😉</label>
        </div>
      </div>
    </form>
    <div class="timer"></div>
    <form class="overlay" onSubmit="return startEsquisse(this)">
      <h3>Esquissé !</h2>
      <label>Aujourd'hui, nous vous proposons un jeu collectif, sans points, dont vous verrez le résultat sur cette page demain !</label>
      <div class="alreadyPlayed" style="display: none">
        <label>Vous avez déjà joué à ce jeu 😉</label>
      </div>
      <div class="lockFree" style="display: none">
        <label>Un seul joueur peut jouer à la fois.</label>
        <label>Quand vous serez prêt, entrez votre nom et cliquez sur le bouton.</label>
        <label>Vous aurez alors ${ESQUISSE_GAME_TIME_IN_MINS}min pour accomplir un tour du jeu <a target="_blank" href="https://www.jeux-goliath.com/produit/esquisse/">Esquissé</a>.</label>
        <label>(pas besoin de connaître la règle pour jouer)</label>
        <input type="text" name="playerName" minlength="3"></input>
        <input type="submit" value="🎬"></input>
      </div>
      <div class="lockTaken" style="display: none">
        <label>Un seul joueur peut jouer à la fois.</label>
        <label>Un joueur est en déjà train de jouer (<span class="lockPlayerName"></span>).</label>
        <label>Revenez un peu plus tard ! 😉</label>
      </div>
    </form>`);
  if (hasChallengeBeenPlayed(esquisse.id)) {
    const alreadyPlayed = esquisse.getElementsByClassName('alreadyPlayed')[0];
    alreadyPlayed.style.display = 'block';
    return;
  }
  regularlyCheckEsquisseLock(esquisse);
});
function regularlyCheckEsquisseLock(esquisse) {
  const overlay = esquisse.getElementsByClassName('overlay')[0];
  if (overlay.style.display !== 'none') {
    const lockFree = overlay.getElementsByClassName('lockFree')[0];
    const lockTaken = overlay.getElementsByClassName('lockTaken')[0];
    getLockState(esquisse.id).then(lock => {
      if (lock) {
        lockFree.style.display = 'none';
        lockTaken.style.display = 'block';
        overlay.getElementsByClassName('lockPlayerName')[0].textContent = lock.playerName;
      } else {
        lockFree.style.display = 'block';
        lockTaken.style.display = 'none';
      }
    });
  }
  setTimeout(regularlyCheckEsquisseLock, 5000, esquisse);
}
function getLockState(lockId) {
  const now = firebase.firestore.Timestamp.now();
  return lockCollec.doc(lockId).get().then(lock => {
    if (!lock.exists || !lock.data().playerName) {
      return null;
    }
    // We auto-expire any lock set for more than ESQUISSE_GAME_TIME_IN_MINS ago by any player:
    if (now - lock.data().start > ESQUISSE_GAME_TIME_IN_MINS*60) {
      lockCollec.doc(lockId).set({playerName: null, start: null});
      return null;
    }
    return lock.data();
  });
}
function acquireLock(lockId, playerName) {
  const start = firebase.firestore.Timestamp.now();
  lockCollec.doc(lockId).set({playerName, start})
}
function startEsquisse(overlayForm) {
  const esquisse = overlayForm.parentNode;
  esquisse.playerName = overlayForm.querySelector('input[type="text"]').value.trim();
  acquireLock(esquisse.id, esquisse.playerName);
  overlayForm.style.display = 'none';
  getPrevGuessAndDrawing().then(({drawing, guess}) => {
    const guessCanvas = esquisse.getElementsByTagName('canvas')[0];
    loadDataURLOntoCanvas(drawing, guessCanvas);
    esquisse.getElementsByClassName('drawingTitle')[0].textContent = guess;
    const drawingCanvas = esquisse.getElementsByTagName('canvas')[1];
    drawingCanvas.prevX = -1;
    drawingCanvas.prevY = -1;
    drawingCanvas.addEventListener('mousemove', e => draw(drawingCanvas, e), false);
    drawingCanvas.addEventListener('mousedown', e => draw(drawingCanvas, e, true), false);
    drawingCanvas.addEventListener('mouseup', e => draw(drawingCanvas, e, false), false);
    drawingCanvas.addEventListener('mouseout', e => draw(drawingCanvas, e, false), false);
    chrono(esquisse.getElementsByClassName('timer')[0], new Date());
  });
  return false;
}
function getPrevGuessAndDrawing() {
  return esquissesCollec.orderBy('timestamp', 'desc').limit(1).get().then(query => query.docs[0].data());
}
function loadDataURLOntoCanvas(strDataURI, guessCanvas) {
  const ctx = guessCanvas.getContext('2d');
  const img = new Image();
  img.onload = () => ctx.drawImage(img, 0, 0);
  img.src = strDataURI;
}
function chrono(timerElem, startTime) {
  let remaingSeconds = ESQUISSE_GAME_TIME_IN_MINS * 60 - Math.floor((new Date() - startTime) / 1000);
  timerElem.textContent = `${Math.floor(remaingSeconds / 60)}:${(remaingSeconds % 60 + '').padStart(2, '0')}`;
  setTimeout(chrono, 1000, timerElem, startTime);
}
function clearDrawing(button) {
  const form = button.parentNode;
  const canvas = form.getElementsByTagName('canvas')[0];
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}
function submitDrawingAndGuess(form) {
  const esquisse = form.parentNode;
  const guess = form.querySelector('input[type="text"]').value;
  const drawing = form.getElementsByTagName('canvas')[1].toDataURL();
  const timestamp = firebase.firestore.Timestamp.now();
  esquissesCollec.doc(esquisse.playerName).set({drawing, guess, timestamp}).then(() => {
    setChallengePlayed(esquisse.id);
    esquisse.getElementsByClassName('drawing-guess-submitted')[0].style.display = 'block';
  });
  return false;
}
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
function hasChallengeBeenPlayed(challengeId) {
  return getCookieAsJSON().challengesPlayed.includes(challengeId);
}
function setChallengePlayed(challengeId) {
  const jsonCookie = getCookieAsJSON();
  jsonCookie.challengesPlayed.push(challengeId);
  storeJSONasCookie(jsonCookie);
}
function getCookieAsJSON() {
  const matchingCookie = document.cookie.split(';').find(cookieStr => cookieStr.startsWith('enigmesEnConfinement='));
  return matchingCookie ? JSON.parse(matchingCookie.split('=', 2)[1]) : {challengesPlayed: []};
}
function storeJSONasCookie(data) {
  document.cookie = 'enigmesEnConfinement=' + JSON.stringify(data);
}
if (document.getElementById('highscores')) {
  updateScoreBoardTable();
}

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
  console.log(slugify(answer));
  digestMessage(slugify(answer)).then(hash => {
    if (form.dataset.hash && hash === form.dataset.hash) {
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
  s = s.replace(/^la-/g, '').replace(/^le-/g, '').replace(/-d-/g, '-').replace(/-st-/g, '-saint-')
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

const esquisses = document.getElementById('esquisses');
if (esquisses) {
  let swap = false;
  esquissesCollec.orderBy('timestamp').get().then(query => query.forEach(doc => {
    let [val1, val2] = [`<canvas width="400" height="400"></canvas>`, doc.data().guess];
    if (swap) [val1, val2] = [val2, val1];
    esquisses.appendChild(htmlTableRow([doc.id, val1, val2]));
    swap = !swap;
    loadDataURLOntoCanvas(doc.data().drawing, last(esquisses.getElementsByTagName('canvas')));
  }));
}
function last(list) { return list[list.length - 1]; }
