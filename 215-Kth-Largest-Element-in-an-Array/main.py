import heapq
from typing import List


class Solution1:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		heapq.heapify(nums)

		while len(nums) > k:
			heapq.heappop(nums)

		return nums[0]


# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
class Solution2:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		nums.sort()

		return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution3:
	# `partition` sorts the array based on the current pivot with respect to the boundaries formed by left and right
	# pointers and returns the index of the pivot after swapping it with the fill pointer. The fill pointer points to
	# the last element that was swapped because it was less than the pivot. Note: Since everytime the subarray that
	# we're looking at, changes, we pass in two variables, the l and r pointer which tell us on which portion of the
	# arr are we currently running quickselect on?
	def partition(self, nums: List[int], left: int, right: int) -> int:
		pivot, fill = nums[right], left

		for i in range(left, right):
			if nums[i] <= pivot:
				nums[fill], nums[i] = nums[i], nums[fill]
				fill += 1

		nums[fill], nums[right] = nums[right], nums[fill]

		return fill

	def findKthLargest(self, nums: List[int], k: int) -> int:
		# We want k as an index. So re-assign it to len(nums) - k
		k = len(nums) - k
		left, right = 0, len(nums) - 1

		# each time the left and right pointers gets closer to each other, we only sort the subarray using those pointers.
		while left < right:
			pivot = self.partition(nums, left, right)

			if pivot < k:
				left = pivot + 1
			elif pivot > k:
				right = pivot - 1
			else:
				break

		return nums[k]


# The same as Solution4, but this is from the video not the neetcode website solution
# Some of the test cases on leetcode are poor cases for quickselect. So this solution is not efficient on leetcode. But this algo
# in average case does beat the quicksort.
class Solution4:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		# We want k as an index. So re-assign it to len(nums) - k
		k = len(nums) - k

		def quickSelect(l, r):
			pivot, p = nums[r], l

			# the second arg of range() is non-inclusive and that's what we want, because we don't want to also iterate on the pivot
			for i in range(l, r):
				if nums[i] <= pivot:
					nums[p], nums[i] = nums[i], nums[p]
					p += 1

			# swap the pivot(or nums[r]) with the p index
			nums[p], nums[r] = nums[r], nums[p]

			# we potentially may have found the solution or we may not
			if p > k:
				# we have to run quickselect on the left portion of the arr because we have to
				return quickSelect(l, p - 1)
			elif p < k:
				return quickSelect(p + 1, r)
			else:
				# here, we know for sure p is the kth largest element
				return nums[p]

		return quickSelect(0, len(nums) - 1)

		# since all of the cases handle all possible cases and they all return sth, we don't need a return at the end