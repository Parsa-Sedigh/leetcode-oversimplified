import heapq
from typing import List


class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		# Initially a heap is just a list in python, later, we will heapify the initialized list
		minHeap = []

		for x, y in points: # O(n)
			dist = (x ** 2) + (y ** 2) # we don't need to take the square root!
			minHeap.append((dist, x, y)) # python will use the first value of the list in the heap.

		# O(n) - turn the list into a min heap, it will reorder the list to make sure that it is in the structure of a heap
		heapq.heapify(minHeap)
		res = []

		# for _ in range(k):
		# 	_, x, y = heapq.heappop(minHeap)
		# 	res.append((x, y))
		# OR:
		while k > 0:
			_, x, y = heapq.heappop(minHeap)
			res.append([x, y])
			k -= 1

		return res