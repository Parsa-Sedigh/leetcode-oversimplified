from typing import List

# Time: O(n)
# Space: O(1)
class Solution1:
	def sortColors(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		l, r = 0, len(nums) - 1
		i = 0

		def swap(i, j):
			tmp = nums[i]
			nums[i] = nums[j]
			nums[j] = tmp

		while i <= r:
			if nums[i] == 0:
				swap(l, i)
				l += 1

			elif nums[i] == 2:
				swap(i, r)
				r -= 1

				# we did this because we have a i+=1 executed for all the cases, but we don't want to increment i if we encountered
				# a 2. So we do this to compensate.
				i -= 1

			i += 1


class Solution2:
	def sortColors(self, nums: List[int]) -> None:
		low = 0
		high = len(nums) - 1
		mid = 0

		while mid <= high:
			if nums[mid] == 0:
				nums[low], nums[mid] = nums[mid], nums[low]
				low += 1
				mid += 1
			elif nums[mid] == 1:
				mid +=1
			else:
				nums[mid], nums[high] = nums[high], nums[mid]
				high -= 1