import heapq


class KthLargest:

	def __init__(self, k: int, nums: List[int]):
		# minHeap with k largest integers
		# Right now, minHeap is just an array, we want to turn it into a heap in the next lines
		self.minHeap, self.k = nums, k

		# Turn minHeap array into an actual heap:
		heapq.heapify(self.minHeap) # Heapify is O(n)

		# We could have more than k elements in our minheap, so pop them:
		while len(self.minHeap) > k:
			heapq.heappop(self.minHeap)

	def add(self, val: int) -> int:
		# There are multiple ways to write the add function but the easiest way is to just add val into our minHeap regardless of
		# what it is, if it's too big, or if it's too small, who cares?
		heapq.heappush(self.minHeap, val)

		if len(self.minHeap) > self.k:
			# Pop the smallest value which MIGHT end up being the `val` or it might end up being a different value
			heapq.heappop(self.minHeap)

		# the minimum value will always be stored in the zeroth index(yeah in OUR implementations of heap, the zeroth index is dummy,
		# but in python standard library, the zeroth index is actually the root, so this is correct here)
		return self.minHeap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)