class ListNode:
	def __int__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		prev, curr = None, head

		while curr:
			nxt = curr.next

			curr.next = prev
			prev = curr
			curr = nxt

		return prev

	def reverseListRecursive(self, head: ListNode) -> ListNode:
		# recursive: T O(n), M O(n)

		# the base case
		if not head:
			return None

		newHead = head

		if head.next:
			newHead = self.reverseListRecursive(head.next)

			# reverse the link between the next node(head.next) and head
			head.next.next = head

		# if head happens to be the first node in the list, it would become the last one in the reversed list, so set it's next to None
		head.next = None

		return newHead
