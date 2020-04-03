Title: Test Esquissé
Tags: lang:fr, enigme, jeux
Slug: test-esquisse
Status: hidden
---

<link rel="stylesheet" type="text/css" href="images/enigmes/enigmes-en-confinement.css">

## ? avril - Esquissé

<div id="challenge-2020-04-31" class="esquisse"></div>


<!--
## Chaînes réalisées

<table>
  <thead><tr> <th>Joueur</th> <th>Chaine A</th> <th>Chaine B</th> </tr></thead>
  <tbody id="esquisses" data-challenge-id="challenge-2020-04-31"></tbody>
</table>
-->

<pre></pre>

<script src="https://www.gstatic.com/firebasejs/7.12.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/7.12.0/firebase-firestore.js"></script>
<script src="https://unpkg.com/imagesloaded@4/imagesloaded.pkgd.min.js"></script>
<script src="images/enigmes/enigmes-en-confinement.js"></script>
<script>
const preElem = document.getElementsByTagName('pre')[0];
document.addEventListener('drawingCanvasReady', () => {
  const drawingCanvas = document.getElementsByTagName('canvas')[1];
  drawingCanvas.addEventListener('mousemove', e => { preElem.innerHTML += 'mousemove\n'; }, false);
  drawingCanvas.addEventListener('mousedown', e => { preElem.innerHTML += 'mousedown\n'; }, false);
  drawingCanvas.addEventListener('mouseup', e => { preElem.innerHTML += 'mouseup\n'; }, false);
  drawingCanvas.addEventListener('touchstart', e => { preElem.innerHTML += 'touchstart\n'; }, false);
  drawingCanvas.addEventListener('touchmove', e => { preElem.innerHTML += 'touchmove\n'; }, false);
  drawingCanvas.addEventListener('touchend', e => { preElem.innerHTML += 'touchend\n'; }, false);
});
</script>