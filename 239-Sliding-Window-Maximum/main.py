import collections
from typing import List


class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		output = []
		q = collections.deque() # contain indexes
		l = r = 0

		while r < len(nums):
			# Make sure no smaller values exist in the queue, before adding the current value to the queue
			# Note: while q and nums[q[-1]] < nums[r] means while queue is not empty and the top value(right most) in the queue, is
			# less than the value that we wanna insert(nums[r]), in other words, while smaller values than current val exist in the queue,
			# we wanna pop from the queue
			while q and nums[q[-1]] < nums[r]:
				q.pop()

			q.append(r)

			# remove the left value from the window. If left value is out of bounds of our window, we have to remove that.
			# Note: q[0] represents an index of the array, that's why we compared it to `l`
			if l > q[0]:
				q.popleft()

			# edge case: Since we're starting l and r being both at 0, we have to check that our window is at least size `k`:
			if (r + 1) >= k:
				output.append(nums[q[0]])

				# l pointer is only gonna be incremented once our window is at least size k. Since both l and r start at
				# index 0, we have to put the incrementation of l, inside this if block
				l += 1

			r += 1

		return output

