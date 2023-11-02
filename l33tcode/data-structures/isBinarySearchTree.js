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

var BSTIterator = function (root) {
    var result = [];
    function inOrderTraversal(node) {
        if (node.left) {
            inOrderTraversal(node.left);
        }
        result.push(node.val);
        if (node.right) {
            inOrderTraversal(node.right);
        }
    }
    inOrderTraversal(root);
    return result;
};
BSTIterator.prototype.next = function () {
    return result.shift();
};
BSTIterator.prototype.hasNext = function() {
    return (result.length > 0);
};

var obj = new BSTIterator(rootn);
var testNext = obj.next();
