from typing import List


class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		# create a set from the initial array nums
		numSet = set(nums)

		# keep track of what the longest consecutive sequence is
		longest = 0

		for n in nums:
			# check if it's the start of a sequence.
			# If current number doesn't have a left neighbour, that means it's start of a sequence
			# Only start the inner loop IF `n` is start of a sequence. Otherwise, we would skip n.
			if (n - 1) not in numSet:
				length = 0

				# keep getting next consecutive number and check if it exists in our numSet, if it does, keep adding to `length`.
				# Note: Initially length is 0, so we're checking if the current number exist in the numSet. As length grows, we'll check
				# next consecutive numbers that if they exist in the numSet
				while (n + length) in numSet:
					length += 1

				# at this point, we could've potentially found the longest sequence, so we wanna potentially update our `longest`
				longest = max(length, longest)

		return longest
