Array.from(document.getElementsByClassName('topoloku')).forEach((table) => {
    const [width, height] = JSON.parse(table.dataset.size);
    const initialLetters = JSON.parse(table.dataset.initialLetters);
    const missingLetters = table.dataset.missingLetters;
    const secretWord = table.dataset.secretWord && JSON.parse(table.dataset.secretWord);
    for (let j = 0; j < height; j++) {
        const tr = document.createElement('tr');
        for (let i = 0; i < width; i++) {
            const td = document.createElement('td');
            td.textContent = initialLetters[`${i},${j}`];
            if (td.textContent) {
                td.classList.add('given');
            } else {
                td.innerHTML = `<input type="text" size="1" maxlength="1">`;
            }
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    if (missingLetters) {
        const missingLettersDiv = document.createElement('div');
        missingLettersDiv.classList.add('missing-letters');
        missingLettersDiv.textContent = `(lettres manquantes: ${missingLetters.split('').join(', ')})`;
        table.after(missingLettersDiv);
    }
    const solutionGrid = solveTopoloku(width, height, initialLetters, missingLetters);
    console.log(solutionGrid);
    // TODO: check if solution OK + call onSuccess + display secretWord
});

function solveTopoloku(width, height, initialLetters, missingLetters) {
    const grid = [ ...Array(width) ].map(() => [ ...Array(height) ]);
    Object.keys(initialLetters).forEach(posStr => {
        const [x, y] = posStr.split(',').map(Number);
        grid[x][y] = initialLetters[posStr];
    });
    // TODO
    return grid;
}