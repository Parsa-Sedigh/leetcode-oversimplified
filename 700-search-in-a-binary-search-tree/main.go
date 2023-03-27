package search_in_a_binary_search_tree

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
	return BFS(root, val)
}

func BFS(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return root
	}

	currNode := root
	var list []*TreeNode
	var queue []*TreeNode

	queue = append(queue, currNode)

	for len(queue) > 0 {
		fmt.Println("hello", len(queue))
		currNode, queue = queue[0], queue[1:]
		fmt.Println("hello 2", len(queue))

		if currNode.Val == val {
			return currNode
		}

		list = append(list, currNode)

		if currNode.Left != nil {
			queue = append(queue, currNode.Left)
		}

		if currNode.Right != nil {
			queue = append(queue, currNode.Right)
		}
	}

	return nil
}
