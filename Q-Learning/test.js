maze_str = [
    '* *********',
    '* x** t* f*',
    '*   x ** **',
    '*f  *    x*',
    '*** ** ****',
    '*t  *   *f*',
    '***  **  x*',
    '  *f *    *',
    '* **   ****',
    '*    *   t*',
    '***********',
];

maze = [];
for(let each of maze_str) {
    line = [];
    for(let letter of each) {
        line.push(letter);
    }
    // console.log(line);
    maze.push(line);
}

console.log(maze)