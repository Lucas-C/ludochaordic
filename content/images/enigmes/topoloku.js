(function() {

const LETTERS_TOPO = {
    'C': {loops: 0, ends: 2},
    'E': {loops: 0, ends: 3},
    'H': {loops: 0, ends: 4},
    '🞯': {loops: 0, ends: 5},
    '✱': {loops: 0, ends: 6},
    'O': {loops: 1, ends: 0},
    'A': {loops: 1, ends: 2},
    '♀': {loops: 1, ends: 3},
    '⦻': {loops: 1, ends: 4},
    '☆': {loops: 1, ends: 5},
    '#': {loops: 1, ends: 8},
    'B': {loops: 2, ends: 0},
    '%': {loops: 2, ends: 2},
    // Isomorphes :
    '&': {loops: 2, ends: 2},
    'D': {loops: 1, ends: 0},
    'F': {loops: 0, ends: 3},
    'G': {loops: 0, ends: 2},
    'K': {loops: 0, ends: 4},
    'L': {loops: 0, ends: 2},
    'M': {loops: 0, ends: 2},
    'N': {loops: 0, ends: 2},
    'P': {loops: 1, ends: 1}, // only character to have 1 end, but equivalent to D in terms of gameplay
    'R': {loops: 1, ends: 2},
    'S': {loops: 0, ends: 2},
    'T': {loops: 0, ends: 3},
    'U': {loops: 0, ends: 2},
    'V': {loops: 0, ends: 2},
    'W': {loops: 0, ends: 2},
    'X': {loops: 0, ends: 4},
    'Y': {loops: 0, ends: 3},
    'Z': {loops: 0, ends: 2},
    // I, J & Q skipped because font matter too much
};

Array.from(document.getElementsByClassName('topoloku')).forEach((table) => {
    const [width, height] = JSON.parse(table.dataset.size);
    const initialLetters = JSON.parse(table.dataset.initialLetters || '{}');
    const missingLetters = (table.dataset.missingLetters || '').split('');
    const secretWordPos = table.dataset.secretWordPos && JSON.parse(table.dataset.secretWordPos);
    const onSuccess = table.dataset.onSuccess;
    for (let j = 0; j < height; j++) {
        const tr = document.createElement('tr');
        for (let i = 0; i < width; i++) {
            const td = document.createElement('td');
            td.textContent = initialLetters[`${i},${j}`];
            if (td.textContent) {
                td.classList.add('given');
            } else {
                td.classList.add('clickable');
                td.onclick = function onTdClick() {
                    this.textContent = allUniqueLetters[allUniqueLetters.indexOf(this.textContent) + 1] || '';
                    if (gridToString(gridFromTable(table)) === solution) {
                        table.classList.add('success');
                        if (secretWordPos) {
                            // TODO
                        }
                        if (onSuccess) (function () { eval(onSuccess); }).call(table);
                    }
                }
            }
            tr.appendChild(td);
        }
        table.appendChild(tr);
    }
    if (missingLetters.length) {
        const missingLettersDiv = document.createElement('div');
        missingLettersDiv.classList.add('topoloku-missing-letters');
        missingLettersDiv.textContent = `(à rajouter: ${missingLetters.join(', ')})`;
        table.after(missingLettersDiv);
    }
    let allUniqueLetters = new Set(Object.values(initialLetters));
    for (let letter of missingLetters) {
        allUniqueLetters.add(letter);
    }
    allUniqueLetters = Array.from(allUniqueLetters);
    const solution = gridToString(solveTopoloku(width, height, initialLetters, allUniqueLetters));
});

function gridFromTable(table) {
    let grid = null;
    const trs = Array.from(table.getElementsByTagName('tr'));
    trs.forEach((tr, j) => {
        if (!grid) {
            grid = [ ...Array(tr.children.length) ].map(() => [ ...Array(trs.length) ]);
        }
        Array.from(tr.children).forEach((cell, i) => {
            grid[i][j] = cell.textContent
        });
    });
    return grid;
}

function solveTopoloku(width, height, initialLetters, allUniqueLetters) {
    const grid = [ ...Array(width) ].map(() => [ ...Array(height) ]);
    Object.keys(initialLetters).forEach(posStr => {
        const [x, y] = posStr.split(',').map(Number);
        grid[x][y] = initialLetters[posStr];
    });
    const grids = [ ...recurAddLetter(grid, allUniqueLetters, [...getEmptyCellPos(grid)]) ];
    if (!grids.length) {
        throw new Error('Zero solution found');
    }
    if (grids.length > 1) {
        grids.map(grid => console.log(gridToString(grid)));
        throw new Error('Several solutions exist');
    }
    return grids[0];
}
function * getEmptyCellPos(grid) {
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (!grid[i][j]) {
                yield [i, j];
            }
        }
    }
}
function * recurAddLetter(grid, letters, emptyCellsPos) { // Brute-force approach
    if (!emptyCellsPos.length) {
        if (isEndsConstraintSatisfied(grid)) {
            yield deepCopy(grid);
        }
        return;
    }
    const [i, j] = emptyCellsPos[0];
    emptyCellsPos = emptyCellsPos.slice(1);
    const edgesCount = [i === 0, j === 0, i === (grid.length - 1), j === (grid[0].length - 1)].filter(x => x).length;
    for (let letter of letters) {
        if (edgesCount >= LETTERS_TOPO[letter].loops) {
            grid[i][j] = letter;
            yield * recurAddLetter(grid, letters, emptyCellsPos)
        }
    }
}
function isEndsConstraintSatisfied(grid) {
    for (let group of groupByContiguousLetters(grid)) {
        const {letter, size} = group;
        if ((LETTERS_TOPO[letter].ends || 1) !== size) {
            return false;
        }
    }
    return true;
}
function groupByContiguousLetters(grid) {
    const groupByPos = {};
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (!groupByPos[`${i},${j}`]) {
                const letter = grid[i][j];
                const groupPos = new Set();
                gatherGroupPos(groupPos, letter, grid, i, j)
                const group = { letter, size: groupPos.size };
                for (let pos of groupPos) {
                    groupByPos[pos] = group;
                }
            }
        }
    }
    return Object.values(groupByPos);
}
function gatherGroupPos(groupPos, letter, grid, i, j) {
    groupPos.add(`${i},${j}`);
    if (i > 0 && !groupPos.has(`${i-1},${j}`) && grid[i-1][j] === letter) {
        gatherGroupPos(groupPos, letter, grid, i - 1, j);
    }
    if (i < (grid.length - 1) && !groupPos.has(`${i+1},${j}`) && grid[i+1][j] === letter) {
        gatherGroupPos(groupPos, letter, grid, i + 1, j);
    }
    if (j > 0 && !groupPos.has(`${i},${j-1}`) && grid[i][j-1] === letter) {
        gatherGroupPos(groupPos, letter, grid, i, j - 1);
    }
    if (j < (grid[0].length - 1) && !groupPos.has(`${i},${j+1}`) && grid[i][j+1] === letter) {
        gatherGroupPos(groupPos, letter, grid, i, j + 1);
    }
}
function gridToString(grid) {
    const rows = [];
    for (let j = 0; j < grid[0].length; j++) {
        let row = '';
        for (let i = 0; i < grid.length; i++) {
            row += grid[i][j];
        }
        rows.push(row);
    }
    return rows.join('\n');
}
function deepCopy(grid) {
  return JSON.parse(JSON.stringify(grid));
}

})();