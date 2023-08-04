// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
    const queue = [];
    const res = [];

    if (root) {
        queue.push(root)
    }

    while (queue.length) {
        const queueLength = queue.length // get the length pf queue before adding the left and right nodes to it
        const currLevel = []

        for (let i = 0; i < queueLength; i++) {
            const current = queue.shift()
            currLevel.push(current.val)

            if (current.left) {
                queue.push(current.left)
            }

            if (current.right) {
                queue.push(current.right)
            }
        }

        res.push(currLevel)
    }

    return res
};