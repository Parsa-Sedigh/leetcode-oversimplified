class Solution:
	def isValid(self, s: str) -> bool:
		stack = []

		# note that the keys are CLOSING chars. This will make this easier.
		closeToOpen = {
			")": "(",
			"]": "[",
			"}": "{"
		}

		for c in s:

			# check if this character is a closing char(the keys of closeToOpen is a closing char)
			if c in closeToOpen:
				# The character is a closing char, so make sure the stack is not empty, because we can't have a closing
				# char in an empty stack. Also we wanna make sure the value at the top of the stack is the matching opening
				# char.
				if stack and stack[-1] == closeToOpen[c]:
					stack.pop()
				else:
					return False

			else:
				stack.append(c)

		return True if not stack else False


# my solution
class Solution2:
	def isValid(self, s: str) -> bool:
		stack = []
		mapping = {
			"(": ")",
			"{": "}",
			"[": "]"
		}

		for el in s:
			if el in mapping:
				stack.append(el)
			else:
				if not stack:
					return False

				last = stack.pop()

				if mapping[last] != el:
					return False

		return len(stack) == 0