package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	cur := dummy
	var carry int

	// if any of these conditions are true, we wanna continue
	for l1 != nil || l2 != nil || carry == 1 {
		var (
			v1 int
			v2 int
		)

		if l1 != nil {
			v1 = l1.Val
		}

		if l2 != nil {
			v2 = l2.Val
		}

		val := v1 + v2 + carry
		carry = val / 10
		val = val % 10

		cur.Next = &ListNode{Val: val}
		cur = cur.Next

		// l1 and l2 could be of different sizes. So each time we need to check if l1 or l2 are done
		if l1 != nil {
			l1 = l1.Next
		}

		if l2 != nil {
			l2 = l2.Next
		}
	}

	return dummy.Next
}
