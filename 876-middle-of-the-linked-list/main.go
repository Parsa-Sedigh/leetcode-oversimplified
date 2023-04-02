package problem876

type ListNode struct {
	Val  int
	Next *ListNode
}

//func middleNode(head *ListNode) *ListNode {
//	var length int
//	currNode := head
//
//	for currNode.Next != nil {
//		length++
//		currNode = currNode.Next
//	}
//
//	isLengthEven := length%2 == 0
//	middle := int(math.Floor(float64(length / 2)))
//
//	if isLengthEven {
//		middle = middle - 1
//	}
//
//	currNode = head
//
//	for i := 0; i <= middle; i++ {
//		currNode = currNode.Next
//	}
//
//	return currNode
//}

func middleNode(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}

	slow := head
	fast := head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	return slow
}
