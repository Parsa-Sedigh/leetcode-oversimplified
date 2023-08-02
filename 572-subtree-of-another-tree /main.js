//  Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

///////////////// brute force solution /////////////////
const checkIfSame = (root, subRoot) => {
    if (!root && !subRoot) return true

    if (!root || !subRoot) return false

    if (root.val !== subRoot.val) return false

    return checkIfSame(root.left, subRoot.left) && checkIfSame(root.right, subRoot.right)
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
    if (!root || !subRoot) {
        return false
    }

    return checkIfSame(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
};
///////////////// /////////////////