from typing import List


class Solution:
	def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
		pair = [[p, s] for p, s in zip(position, speed)]  # this is called list comprehension in python

		# will tell us how many car fleets we have at the end
		stack = []

		# we want to iterate through it in reverse order, so use [::-1]
		for p, s in sorted(pair)[::-1]: # reverse sorted order
			stack.append((target - p) / s)

			if len(stack) >= 2 and stack[-1] <= stack[-2]:
				stack.pop()

		return len(stack)