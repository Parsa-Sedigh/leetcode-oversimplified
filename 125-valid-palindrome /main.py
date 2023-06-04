class Solution:
	def isPalindrome(self, s: str) -> bool:
		l, r = 0, len(s) - 1

		while l < r:
			# we need to make sure l stays inside the bounds of string and also never passes the right pointer, so while it's not alphanumeric,
			# move it forward until it is before r
			while l < r and not not self.alphaNum(s[l]):
				l += 1

			while r > l and not not self.alphaNum(s[r]):
				r -= 1

			if s[l].lower() != s[r].lower():
				return False

			l, r = l + 1, r - 1

		return True

	def alphaNum(self, c):
		return (ord('A') <= ord(c) <= ord('Z') or
				ord('a') <= ord(c) <= ord('z') or
				ord('0') <= ord(c) <= ord('9'))
