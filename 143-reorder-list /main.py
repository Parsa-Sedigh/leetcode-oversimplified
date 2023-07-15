class ListNode:
	def __int__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def reorderList(self, head: ListNode) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""

		# First, find the middle point of the list, so we need two pointers, one slow and one fast
		slow, fast = head, head.next

		# while fast is not null and fast has not reached the end of the list:
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		# at this point, we have the beginning of the second half of the list which is gonna be the `slow.next`.
		second = slow.next

		# now we have to reverse the second half of the list, but before doing that we need to set slow.next to None, because
		# that slow pointer is gonna become the end of the reordered list(we're splitting the portions).
		slow.next = None

		# at the beginning prev is None and on each iteration, it will be the prev node that we visited so we still have a reference to it in order to
		# reverse the list
		prev = None

		# reverse the second portion of the linked list
		while second:
			tmp = second.next
			second.next = prev
			prev = second
			second = tmp

		# at this point, the second half is reversed, now we have to merge the two halfs of the list
		# Note: The beginning of the second list is gonna be prev. Because after the previous loop was done, second is gonna be
		# set to None, but `prev` is going to be set to whatever the last node that we looked at was and whatever that last node was, is actually
		# gonna be the new head of the second half of the list. In other words, after the loop, as we move forward and reverse the nodes,
		# prev will be the new head of the second reversed list.

		# merge two halfs
		first, second = head, prev

		# we're gonna keep going until one of the pointers is null, so condition would be(first and second), but we also know that the
		# second half of the list could be shorter than the first half(first half would never be shorter than the second half), so we just
		# use `second` as the condition:
		while second:
			# store next nodes of `first` and `second` into temporary variables because we know we're gonna breaking those links between the nodes
			tmp1, tmp2 = first.next, second.next

			first.next = second
			second.next = tmp1

			first = tmp1
			second = tmp2
