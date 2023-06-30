from typing import List


class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		res = [0] * len(temperatures)
		stack = []  # pair: [tmp, index of tmp]

		for i, t in enumerate(temperatures):

			# top of the stack is stack[-1] and the tmp is the first value of the list in that index
			while stack and t > stack[-1][0]:
				stackT, stackInd = stack.pop()
				res[stackInd] = (i - stackInd)

			stack.append([t, i])

		return res
