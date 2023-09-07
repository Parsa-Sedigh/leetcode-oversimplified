class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		count = {}
		res = 0
		l = 0

		for r in range(len(s)):
			count[s[r]] = 1 + count.get(s[r], 0)

			# is the current window valid? We find out by subtracting the length of the window and the count of the most frequent
			# character which is max(count.values()). The max(count.values() is going through the hashmap which could be of size 26,
			# so this operation would be O(26)
			# Note: The number of replacements we have to do for current window is (r - l + 1) - max(count.values()) .
			# Note: Here, instead of while, you can use an if block as well
			while (r - l + 1) - max(count.values()) > k:
				count[s[l]] -= 1
				l += 1


			res = max(res, r - l + 1)

		return res

	def characterReplacement2(self, s: str, k: int) -> int:
		count = {}
		res = 0
		l = 0

		# with this, we don't need to do max(count.values() which is getting the max value of entire hashmap, anymore
		maxF = 0

		for r in range(len(s)):
			count[s[r]] = 1 + count.get(s[r], 0)

			# maybe the new count of s[r] is now the maximum in entire hashmap. Maybe s[r] became the most frequent character now.
			# The max() function is constant time operation(O(1))
			maxF = max(maxF, count[s[r]])

			while (r - l + 1) - maxF > k:
				# Notice that even though we're shifting l pointer, which means we're removing characters from our window and therefore
				# potentially decreasing the value of current maximum number of occurrences in hashmap, we're STILL NOT decrementing maxF(which
				# we can't because we don't know the character that was removed was actually the maximum occurrence char). Because
				# we actually don't need to, it won't end up affecting the result if we don't decrementing it(which could also give us a
				# wrong result). That's why we only needed to store an int for maxF not which character actually has the most occurrences.
				# So this was an optimization which is hard to see why we're allowed to do that.
				count[s[l]] -= 1
				l += 1


			res = max(res, r - l + 1)

		return res