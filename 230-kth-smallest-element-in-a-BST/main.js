//  Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/////////////// In order traversal approach ///////////////

/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function (root, k) {
    const dfs = (node, list) => {
        if (!node) return

        dfs(node.left, list)

        list.push(node.val)

        dfs(node.right, list)

        return list
    }

    const elements = dfs(root, [])

    return elements[k - 1]
};

/////////////// ///////////////