//  Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

///////////// brute force /////////////
const isSmaller = (node, prev) => {
    if (!node) return true

    console.log('smaller:', node.val, prev)

    if (node.val >= prev) return false

    return (isSmaller(node.left, prev) &&
            isSmaller(node.right, prev))
}

const isGreater = (node, prev) => {
    if (!node) return true

    console.log('greater:', node.val, prev)

    if (node.val <= prev) return false

    return (isGreater(node.left, prev) &&
            isGreater(node.right, prev))
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
    if (!root) return true

    return (isSmaller(root.left, root.val) &&
            isGreater(root.right, root.val) &&
            isValidBST(root.left) &&
            isValidBST(root.right))
};

///////////// /////////////