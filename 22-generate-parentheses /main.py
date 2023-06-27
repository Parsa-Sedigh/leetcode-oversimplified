from typing import List


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		# only add open parentheses if open < n
		# only add a closing parentheses if closed < open
		# valid IIF open == closed == n . So we only gonna stop adding parentheses all together if open == closed == n

		stack = []
		res = []  # result

		# openN is number of open parentheses
		def backtrack(openN, closedN):

			# base case
			if openN == closedN == n:
				# join every character in the stack together into an empty string and once they've been joined together, they will
				# form a complete string and we're gonna append that to our result list.
				# In other words, we join all the elements of stack together using an empty string means just stick them together. So
				# we would end up with a sequence of parentheses and then append that sequence to the result list.
				res.append("".join(stack))

				# since this is the base case, we just return
				return

			if openN < n:
				stack.append("(")
				backtrack(openN + 1, closedN)

				# once the previous backtracking returns, we have to update the stack because we only have a single stack variable. Remember we're
				# not passing the stack into every since call, the stack is kinda a global variable.
				stack.pop()

			if closedN < openN:
				stack.append(")")
				backtrack(openN, closedN + 1)

				# cleanup
				stack.pop()

		backtrack(0, 0)

		return res
