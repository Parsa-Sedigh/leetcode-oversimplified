from typing import List


class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		# Let's say we didn't even have a common prefix among any of the strings, they all started with a different character,
		# like [a, b, c], so then we return an empty string
		res = ""

		for i in range(len(strs[0])):
			for s in strs:
				# It could be the case where the strs[0] is a long string and other strings are very short, in that case we would
				# comparing a char of strs[0] with nothing(out of bound) of other shorter strings. So we need to check for this.
				# We can figure this out with `i == len(s)` and if this was true, we would immediately return `res` and end the algo.
				if i == len(s) or s[i] != strs[0][i]:
					return res

			res += strs[0][i]

		return res