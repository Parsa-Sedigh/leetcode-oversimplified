package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	slow, fast := head, head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next

		/* Note: We must put the check after moving slow and fast, because they both start at the head at the beginning and this would cause
		return true immediately as we enter the loop for all the inputs. So put this check after actually moving pointers.*/
		if slow == fast {
			return true
		}
	}

	return false
}
