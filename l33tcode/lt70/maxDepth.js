/*
*Find the maximum Depth of a Binary Tree
*/
function maxDepth(root) {
    var deeps = [];
    function traverse(node, depth) {
        depth += 1;
        if(node.left) {
            traverse(node.left, depth);
        }
        if(node.right) {
            traverse(node.right, depth);
        }
        deeps.push(depth);
    }
    traverse(root, 0);
    return Math.max(...deeps);
};

class Node {
    constructor(val, left, right) {
        this.val = val;
        this.left = (left === undefined) ? null : left;
        this.right = (right === undefined) ? null : right;
    }
};

var leafs = [new Node(3), new Node(9), new Node(20)];
var edge = new Node(15, leafs[1], leafs[2]);
const rootn = new Node(7, leafs[0], edge);

var maxdepth = maxDepth(rootn);
console.log(maxdepth);