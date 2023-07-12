class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		# dummy holds the entire result list(which means it points to the head of the result list). We need another pointer for traversing
		# the result linked list. So we create another variable called tail and initially point it to the head of the result linked list
		# Note that we never update the dummy or move it. Because it should hold the list. Instead we use a helper variable for
		# adding new nodes.
		dummy = ListNode()
		tail = dummy

		while l1 and l2:
			if l1.val < l2.val:
				tail.next = l1
				l1 = l1.next
			else:
				tail.next = l2
				l2 = l2.next

			tail = tail.next

		if l1:
			# take the remaining portion of l1 and add it to the end of the result list which is pointed by the tail variable
			tail.next = l1
		else:
			tail.next = l2

		return dummy.next