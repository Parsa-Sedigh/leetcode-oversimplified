class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		# edge case
		if len(s1) > len(s2): return False

		s1Count, s2Count = [0] * 26, [0] * 26

		for i in range(len(s1)):
			# ord(s1[i]) - ord('a') will map to one of the 26 indexes
			s1Count[ord(s1[i]) - ord('a')] += 1
			s2Count[ord(s2[i]) - ord('a')] += 1

		matches = 0

		for i in range(26):
			# increment it by 1 if s1Count[i] == s2Count[i], else increment it by 0
			matches += (1 if s1Count[i] == s2Count[i] else 0)

		# sliding window
		l = 0

		# we know that don't need to start at the first position of s2, because we've already gone through some of the elements of s2
		# when we were initializing s1Count and SOME of the s2Count(because s2 string is longer or equal to s1, there are still some elements
		# in s2 that we need to look OBVIOUSLY!). So start at the length of s1 because this will start us at the next char that we
		# need to check.
		# Note: As we know, loops are non-inclusive, so when we had range(len(s1)) at the first loop, we didn't iterate over the last index
		# in len(s1). So we need to start from that one until the end of s2.
		for r in range(len(s1), len(s2)):
			# We could put this if statement before this loop, but it will be redundant. We can put it here as first statement of for loop.
			# Because we also need to check it here, so we only write it once here
			if matches == 26:
				return True

			# we have to map the current character to an index of the s2Count array.
			index = ord(s2[r]) - ord('a')
			s2Count[index] += 1

			# Now that we just incremented the count of this char by one, it could be possible that now it exactly equals the count of
			# the same character in s1. If that's the case, we can increment `matches`. But it's possible that also by incrementing
			# the char count, instead of making it equal to the one in s1Count, we made it too large. So we have to decrement the matches
			# in that case(the elif case).
			if s1Count[index] == s2Count[index]:
				matches += 1

			# this case means they WERE equal, but we just incremented s2Count[index], so now we made them unequal
			elif s1Count[index] + 1 == s2Count[index]:
				matches -= 1

			# we removed the character at index `l`.
			index = ord(s2[l]) - ord('a')
			s2Count[index] -= 1

			if s1Count[index] == s2Count[index]:
				matches += 1

			# if by decrementing s2Count[index], we changed it from being exactly equal to the one in s1Count, from now being slightly
			# too small(by 1 actually), meaning it's now equal to s1Count[index] - 1, we're gonna decrement the `matches`.
			elif s1Count[index] - 1 == s2Count[index]:
				matches -= 1

			# We're incrementing l in each iteration, why? Because we know when we start this loop, our size of the window(which is l = 0 and
			# r = len(s1)), is the exact size as we need(it's equal to size of s1). So we need to increase l at each
			# iteration as we increase r as well to preserve the correct size of the window.
			l += 1

		# We can't return False here, because it's possible that after our loop exited, we know that in the LAST iteration of the loop,
		# we didn't check if the matches == 26 . We need to do it here:
		return matches == 26


