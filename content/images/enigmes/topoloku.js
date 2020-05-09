/****************************************************************************
 * DOM rendering
 ****************************************************************************/
export function renderTopolokuUsingDataAttrs(table) {
    const size = JSON.parse(table.dataset.size);
    console.log(renderTopoloku(table, {
        size,
        initialLetters: JSON.parse(table.dataset.initialLetters || '{}'),
        missingLetters: (table.dataset.missingLetters || '').split(''),
        secretWordPos: table.dataset.secretWordPos && JSON.parse(table.dataset.secretWordPos),
        onSuccess: table.dataset.onSuccess && (() => window[table.dataset.onSuccess](table)),
        solution: table.dataset.solution && lineFormatGrid(table.dataset.solution, size[0]),
        solve: table.dataset.solve,
    }));
}
export function renderTopoloku(table, options) {
    const [width, height] = options.size;
    const initialLetters = options.initialLetters || {};
    const missingLetters = options.missingLetters || [];
    const secretWordPos = options.secretWordPos;
    const onSuccess = options.onSuccess;
    let allUniqueLetters = new Set(Object.values(initialLetters));
    for (let letter of missingLetters) {
        allUniqueLetters.add(letter);
    }
    allUniqueLetters.delete('■');
    allUniqueLetters = Array.from(allUniqueLetters).sort();
    for (let j = 0; j < height; j++) {
        const tr = document.createElement('tr');
        for (let i = 0; i < width; i++) {
            const td = document.createElement('td');
            td.textContent = initialLetters[`${i},${j}`];
            if (td.textContent === '■') {
                td.classList.add('black');
            } else if (td.textContent) {
                td.classList.add('given');
            } else {
                td.classList.add('clickable');
                td.onclick = function onTdClick() {
                    this.textContent = allUniqueLetters[allUniqueLetters.indexOf(this.textContent) + 1] || '';
                    table.classList.remove('success');
                    if (secretWordPos) {
                        Array.from(table.getElementsByTagName('td')).forEach(td => td.classList.remove('highlight'));
                    }
                    const grid = gridFromTable(table);
                    if (isLoopsConstraintSatisfied(grid) && isEndsConstraintSatisfied(grid, allUniqueLetters)) {
                        table.classList.add('success');
                        if (secretWordPos) {
                            highlightSecretWord(table, secretWordPos);
                        }
                        if (onSuccess) {
                            onSuccess();
                        }
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
    if (options.solve) {
        return gridToString(solveTopoloku(width, height, initialLetters, allUniqueLetters));
    }
}

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
function lineFormatGrid(str, width) {
    return str.trim().match(new RegExp(`.{1,${width}}`, 'g')).join('\n');
}
function highlightSecretWord(table, secretWordPos, k = 0) {
    if (k >= secretWordPos.length) return;
    const trs = Array.from(table.getElementsByTagName('tr'));
    const [i, j] = secretWordPos[k];
    trs[j].children[i].classList.add('highlight');
    setTimeout(highlightSecretWord, 500, table, secretWordPos, k + 1);
}


/****************************************************************************
 * Portable Ecmascript
 ****************************************************************************/
const LETTERS_TOPO = {
    'C': {loops: 0, ends: 2},
    'E': {loops: 0, ends: 3},
    'H': {loops: 0, ends: 4},
    '🞯': {loops: 0, ends: 5},
    '✱': {loops: 0, ends: 6},
    'O': {loops: 1, ends: 0},
    'A': {loops: 1, ends: 2},
    '♀': {loops: 1, ends: 3},
    '⦷': {loops: 1, ends: 4},
    '☆': {loops: 1, ends: 5},
    '#': {loops: 1, ends: 8},
    'B': {loops: 2, ends: 0},
    '%': {loops: 2, ends: 2},
    // Isomorphes :
    'D': {loops: 1, ends: 0}, // like O
    'F': {loops: 0, ends: 3}, // like E
    'G': {loops: 0, ends: 2}, // like C
    'K': {loops: 0, ends: 4}, // like H
    'I': {loops: 0, ends: 2}, // like C, font matters a lot (Helvetica)
    'J': {loops: 0, ends: 2}, // like C, font matters a lot (Helvetica)
    'L': {loops: 0, ends: 2}, // like C
    'M': {loops: 0, ends: 2}, // like C
    'N': {loops: 0, ends: 2}, // like C
    'P': {loops: 1, ends: 1}, // like O, only character to have 1 end
    'Q': {loops: 1, ends: 2}, // like A, font matters a lot (Helvetica)
    'R': {loops: 1, ends: 2}, // like A
    'S': {loops: 0, ends: 2}, // like C
    'T': {loops: 0, ends: 3}, // like E
    'U': {loops: 0, ends: 2}, // like C
    'V': {loops: 0, ends: 2}, // like C
    'W': {loops: 0, ends: 2}, // like C
    'X': {loops: 0, ends: 4}, // like H
    'Y': {loops: 0, ends: 3}, // like E
    'Z': {loops: 0, ends: 2}, // like C
    '&': {loops: 2, ends: 2}, // like %
    '♡': {loops: 1, ends: 0}, // like O
    '+': {loops: 0, ends: 4}, // like H
    '=': {loops: 0, ends: 4}, // like H
};
export function solveTopoloku(width, height, initialLetters, allUniqueLetters) {
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
        if (isEndsConstraintSatisfied(grid, letters)) {
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
function isEndsConstraintSatisfied(grid, requiredLetters) { // Also checks that all required letters are used
    const gridLetters = new Set();
    for (let group of groupByContiguousLetters(grid)) {
        const {letter, size} = group;
        if ((LETTERS_TOPO[letter].ends || 1) !== size) {
            return false;
        }
        gridLetters.add(letter);
    }
    return gridLetters.size === requiredLetters.length;
}
function groupByContiguousLetters(grid) {
    const groupByPos = {};
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            const letter = grid[i][j];
            if (!groupByPos[`${i},${j}`] && letter !== '■') {
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
function isLoopsConstraintSatisfied(grid) { // Also checks that all cells are filled
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            const edgesCount = [i === 0, j === 0, i === (grid.length - 1), j === (grid[0].length - 1)].filter(x => x).length;
            const letter = grid[i][j];
            if (!letter || letter === '■' || edgesCount < LETTERS_TOPO[letter].loops) {
                return false;
            }
        }
    }
    return true;
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
function gridFromString(str) { // Non testé
    const rows = str.trim().split('\n').map(row => row.trim());
    return [ ...Array(rows[0].length).keys() ].map(i => {
        return [ ...Array(rows.length).keys() ].map(j => rows[j].charAt(i));
    });
}
function deepCopy(grid) { return JSON.parse(JSON.stringify(grid)); }
