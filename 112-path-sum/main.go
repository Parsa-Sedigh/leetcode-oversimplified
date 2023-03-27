package pathsum

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	if root == nil {
		return false
	}

	return dfs(root, targetSum, 0)
}

// we need to pass one more param since the solution func doesn't have.
func dfs(root *TreeNode, targetSum, currSum int) bool {
	if root == nil {
		return false
	}

	currSum += root.Val

	if root.Left == nil && root.Right == nil {
		fmt.Println(root.Val, currSum, targetSum, currSum == targetSum)
		return currSum == targetSum
	}

	// if root.Left != nil {
	// 	return dfs(root.Left, targetSum, currSum)
	// }

	// if root.Right != nil {
	// 	return dfs(root.Right, targetSum, currSum)
	// }

	// return false

	return dfs(root.Left, targetSum, currSum) || dfs(root.Right, targetSum, currSum)
}
