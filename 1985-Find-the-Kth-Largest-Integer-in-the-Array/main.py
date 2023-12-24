import heapq
from typing import List


class Solution:
	def kthLargestNumber(self, nums: List[str], k: int) -> str:
		# Python doesn't have max heaps. We can simulate max heap by placing the values as negative. In this case it's fine,
		# because all the values are gonna be positive, so they can be converted to negative and we would have no problem. With this,
		# when we pop a value, we're kinda popping the max val.
		maxHeap = [-int(n) for n in nums]
		heapq.heapify(maxHeap)  # O(n)

		# If the question has asked the k = 3 largest element, we only want to pop two elements from the max heap to get the
		# third largest element which means: while k > 1 .
		# O(k)
		while k > 1:
			heapq.heappop(maxHeap)  # O(log(n))
			k -= 1

		return str(-maxHeap[0])
