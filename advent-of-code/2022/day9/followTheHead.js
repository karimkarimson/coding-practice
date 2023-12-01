// Day 8 Part 1
/* 
* The Head travels and the Tail follows
Strategy:
1. Make a Graph
2. Each Vertice has 8 Edges: N, NE, E, SE, S, SW, W, NW
3. Each Vertice has a property "visited" set to false
3. The Head travels foreward and creates the Vertices needed
4. The Tail follows and sets the property "visited" to true 
*/

// import the data
const fs = require('fs');
// let file = fs.readFileSync('C:/Users/karim/Desktop/eigeneProjekte/advent-of-code/day9/sample.txt', 'utf8');
let file = fs.readFileSync('C:/Users/karim/Desktop/eigeneProjekte/advent-of-code/day9/input.txt', 'utf8');
file = file.split('\n');
// clean up the commands, each line
const eachLineCleaned = [];
// thank you windows for the \r
file.forEach((cmd) => {
    eachLineCleaned.push(cmd.replace(/(\n\r|\n|\r)/gm, ""));
});
// split direction and distance
const cleanData= [];
eachLineCleaned.forEach((line) => {
   cleanData.push(line.split(" "));
});

// create Vertice class
class Vertice {
    constructor(row, col) {
        this.row = row;
        this.col = col;
        this.visited = false;
        this.r = null;
        this.l = null;
        this.u = null;
        this.d = null;
    }
    setVisited() {
        this.visited = true;
    }
    // set Left, Right, Up, Down - Neighboor Vertices 
    setR(vertice) {
        this.r = vertice;
    }
    setL(vertice) {
        this.l = vertice;
    }
    setU(vertice) {
        this.u = vertice;
    }
    setD(vertice) {
        this.d = vertice;
    }
}

const graphArray = [new Vertice(0, 0)];
var head = graphArray[0];
var headPrevious = graphArray[0];
var tail = graphArray[0];

// logic for head
function headTravel(direction) {
    if (head[direction] === null) {
        [goRow, goColumn] = getDirectionValues(direction);
        head[direction] = new Vertice((head.row + goRow), (head.col + goColumn));
        graphArray.push(head[direction]);
        headPrevious = head;
        head = head[direction];
        head[oppositeDirection(direction)] = headPrevious;
    } else if (pointIsNeighboor()) {
        // point is next to vertice
    } else {
        headPrevious = head;
        head = head[direction];
    };
}
function pointIsNeighboor() {
}
function getDirectionValues(direction) {
    switch(direction) {
        case "r": return [0, 1];
        case "l": return [0, -1];
        case "u": return [-1, 0]; 
        case "d": return [1, 0];
    }
}
function oppositeDirection(direction) {
    switch(direction) {
        case "r": return "l";
        case "l": return "r";
        case "u": return "d";
        case "d": return "u";
    }
}

// logic for tail
function tailFollow() {
    function tailTouches() {
        let deltaRow = Math.abs(tail.row - head.row);
        let deltaCol = Math.abs(tail.col - head.col);
        if (deltaRow < 2 && deltaCol < 2) {
            return true;
        } else {
            return false;
        };
    };
    var isTouching = tailTouches();
    if (!isTouching) {
        // tail isnt touching head, so follow
        /* * logic for tailtravel
        1. calculate deltaRow and deltaCol
        2. if delta > 1, travel in the direction of delta 
        */
       console.warn(`Tail is at ${tail.row}, ${tail.col}`);
       tail = headPrevious;
       tail.setVisited();
    } else {
        // tail touches head, so nothing happens
    };
}
cleanData.forEach((line) => {
    for (let i = 0; i < line[1]; i++) {
        headTravel(line[0].toLowerCase());

        console.log(`Head ist at ${head.row}, ${head.col}`);
        
        // check if tail needs to follow
        tailFollow();
    };
});
var counter = 0;
graphArray.forEach((vertice) => {
    if (vertice.visited === true) {
        counter++;
        console.log(`There are ${counter} Vertices is visited`);
    };
});