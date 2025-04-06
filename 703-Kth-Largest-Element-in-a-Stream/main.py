import heapq
from typing import List

# Min heap
# T: O()

# In the constructor, the while loop runs until the size of the min heap (self.minHeap) becomes equal to or less than k.
# In the worst-case scenario, where len(self.minHeap) is greater than k, the loop will execute until it has reduced the size of
# the heap to k. However, it's important to note that the number of iterations of the while loop is not directly related to
# the size of the input nums list.

# The time complexity of the while loop depends on the number of elements removed from the heap, which is
# at most n - k elements (where n is the number of elements in nums and k is the value of self.k).

# So, the correct time complexity for the while loop would be O(n - k) in the worst case, rather than O(n).
# Considering both the heapq.heappop() operation and the number of iterations of the while loop, the total
# time complexity of the constructor becomes O((n - k) * log n). I GUESS!!!

# M: O(n)
class KthLargest:

	# T: O(n)
	# M: O(n)
	def __init__(self, k: int, nums: List[int]):
		# minHeap with k largest integers
		# Right now, minHeap is just an array, we want to turn it into a heap in the next lines
		self.minHeap, self.k = nums, k

		# Turn minHeap array into an actual heap:
		heapq.heapify(self.minHeap) # Heapify is O(n)

		# T: O((n - k) * log(n))
		# We could have more than k elements in our minheap, so pop them:
		while len(self.minHeap) > k:
			heapq.heappop(self.minHeap)

	# T: O(log(k)) - where k is the size of the heap
	# M: O(1)
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

# Brute force
# T: O()
# M: O()
class KthLargest2:


class KthLargest3:

	# T: O(n * log(n)). Because in py, list.sort() takes O(n * log(n))
	# M: O(n). Note: In py, list.sort() is in place.
	def __init__(self, k: int, nums: List[int]):
		self.k = k
		self.nums = nums
		self.nums.sort()

	# T: O(n)
	# M: O(1)
	def add(self, val: int) -> int:
		l = 0
		r = len(self.nums) - 1

		# T: (log(n))
		while l <= r:
			m = (l + r) // 2

			if val < self.nums[m]:
				r = m - 1
			elif val >= self.nums[m]:
				l = m + 1

		# T: O(n). Inserting into arr takes O(n) in worst case OFC.
		self.nums.insert(l, val)

		return self.nums[len(self.nums) - self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)