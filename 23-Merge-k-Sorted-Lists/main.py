from typing import List


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		if not lists or len(lists) == 0:
			return None

		# take pairs of linked lists and merge them each time and we keep doing this until there's one linked list remaining and that's
		# gonna be our output(lists[0])
		while len(lists) > 1:
			mergedLists = []

			for i in range(0, len(lists), 2):
				l1 = lists[i]

				# if l2 is None, it's still ok because merging one linked list and one null linked list is perfectly fine.
				l2 = lists[i + 1] if (i + 1) < len(lists) else None
				mergedLists.append(self.mergeList(l1, l2))

			lists = mergedLists

		return lists[0]

	# merges two sorted lists
	def mergeList(self, l1, l2):
		dummy = ListNode()
		tail = dummy # tail points to the tail of the merged linked list

		# we must move l1 and l2 pointers themselves forward, so that one of these pointers goes out of bounds. You can use new variables
		# if you don't want to change the function parameters, from a clean code perspective.
		while l1 and l2:
			if l1.val < l2.val:
				tail.next = l1

				# move l1 pointer forward, so that at some point one of l1 or l2 pointers gonna go out of bounds of their
				# respective linked lists.
				l1 = l1.next
			else:
				tail.next = l2
				l2 = l2.next

			# move the tail pointer forward
			tail = tail.next

		if l1:
			# l1 itself is sorted, so we can just point the tail to l1
			tail.next = l1
		if l2:
			tail.next = l2

		return dummy.next
