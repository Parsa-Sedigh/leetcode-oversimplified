package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// My initial solution
// T: O(n)
// M: O(n)
func pairSum(head *ListNode) int {
	f1Nodes := make([]int, 0, 10)
	f2Nodes := make([]int, 0, 10)

	f1, f2 := head, head.Next
	maxVal := 0

	f1Nodes = append(f1Nodes, f1.Val)
	f2Nodes = append(f2Nodes, f2.Val)

	for f2 != nil && f2.Next != nil {
		f1 = f1.Next.Next
		f2 = f2.Next.Next

		f1Nodes = append(f1Nodes, f1.Val)
		f2Nodes = append(f2Nodes, f2.Val)
	}

	for i := 0; i < len(f1Nodes); i++ {
		maxVal = max(maxVal, f1Nodes[i]+f2Nodes[len(f2Nodes)-i-1])
	}

	return maxVal
}

// T: O(n)
// M: O(1)
func pairSum2(head *ListNode) int {
	var prev *ListNode

	prev, slow, fast := nil, head, head

	// T: O(n)
	for fast != nil && fast.Next != nil {
		prev = slow
		slow = slow.Next
		fast = fast.Next.Next
	}

	prev.Next = nil

	var prev2 *ListNode

	// reverses the second half of the linked list. This also takes O(n/2) time, which simplifies to
	// T: O(n).
	for slow != nil {
		nxt := slow.Next
		slow.Next = prev2
		prev2 = slow
		slow = nxt
	}

	maxSum := 0
	head1, head2 := head, prev2

	// T: O(n/2) => O(n)
	for head1 != nil {
		maxSum = max(maxSum, head1.Val+head2.Val)
		head1 = head1.Next
		head2 = head2.Next
	}

	return maxSum
}
