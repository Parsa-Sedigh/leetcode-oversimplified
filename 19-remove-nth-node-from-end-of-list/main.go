package problem19

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	dummyNode := &ListNode{Next: head}
	l := dummyNode
	r := head

	for i := 0; i < n; i++ {
		r = r.Next
	}

	for r != nil {
		l = l.Next
		r = r.Next
	}

	l.Next = l.Next.Next

	fmt.Println("hello", head, dummyNode)

	return dummyNode.Next
}
