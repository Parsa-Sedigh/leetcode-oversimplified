from typing import List


class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []

		for c in tokens:
			if c == "+":
				stack.append(stack.pop() + stack.pop())
			elif c == "-":
				a, b = stack.pop(), stack.pop()
				stack.append(b - a)
			elif c == "*":
				stack.append(stack.pop() * stack.pop())
			elif c == "/":
				a, b = stack.pop(), stack.pop()

				# to round towards zero, use int() which will convert it into integer and also round it towards zero at the same time
				stack.append(int(b / a))
			else:
				stack.append(int(c))

		return stack[0]
