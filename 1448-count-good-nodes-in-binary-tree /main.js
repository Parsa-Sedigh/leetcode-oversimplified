// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var goodNodes = function (root) {
    const dfs = (node, maxVal) => {
        if (!root) return 0

        let res = 0;

        if (node.val >= maxVal) {
            res = 1

            // we can update maxVal here as well
            // maxVal = node.val
        }

        maxVal = Math.max(maxVal, node.val)

        res += dfs(node.left, maxVal)
        res += dfs(node.right, maxVal)

        return res
    }

    return dfs(root, root.val)
};