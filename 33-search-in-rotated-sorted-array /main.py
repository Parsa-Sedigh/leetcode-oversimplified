from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums) - 1

		while l <= r:
			mid = (l + r) // 2

			if target == nums[mid]:
				return mid

			# are we in the left sorted portion?
			if nums[l] <= nums[mid]:
				if target > nums[mid] or target < nums[l]:
					l = mid + 1
				else:  # means target < nums[mid] and target > nums[l] . So target is at the left side of array, so move r to the left side
					r = mid - 1

			# we're in the right sorted portion then
			else:
				if target < nums[mid] or target > nums[r]:
					r = mid - 1
				else:
					l = mid + 1

		return -1
