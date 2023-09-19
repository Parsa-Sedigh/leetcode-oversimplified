class Solution:
	def minWindow(self, s: str, t: str) -> str:
		# handle an edge case
		if t == "": return ""

		# window is current window
		countT, window = {}, {}

		# countT is not gonna change throughout the algo, so let's fill it:
		for c in t:
			countT[c] = 1 + countT.get(c, 0)

		# len(countT) gives us the number of unique characters in the string t(because countT is the map pf unique chars in `t`).
		have, need = 0, len(countT)
		res, resLen = [-1, -1], float("infinity")
		l = 0

		for r in range(len(s)):
			c = s[r]
			window[c] = 1 + window.get(c, 0)

			# we check `c in countT` because we know we don't care about the characters that aren't even in string `t`.
			# Note: First we need to check if current character(c) actually exists in countT(`c in countT`)
			if c in countT and window[c] == countT[c]:
				have += 1

			# While this condition is met, we wanna keep shrinking the window(obviously from left). Why? Because we wanna make find the
			# smallest string that is valid(valid means have == need)
			while have == need:
				# potentially update our result
				# Note: The size of the current window is `r - l + 1`
				# Note: The resLen initially starts at infinity, so this will definitely execute at least once
				if (r - l + 1) < resLen:
					res = [l, r]
					resLen = r - l + 1

				# remove from the left of our window(minimize it - because we want the minimum window length)
				window[s[l]] -= 1

				# Since we removed a character, it's possible that our have and need condition is no longer met:
				# Note: `s[l] in countT` means it's one of the characters that we need to satisfy our condition
				# Note: `window[s[l]] < countT[s[l]]` means somehow right now, for the first time(because we're checking
				# immediately after removing the character), the related count of character in window is less than the
				# count that we need(countT[s[l]]), what we did is we just decremented the `have`
				if s[l] in countT and window[s[l]] < countT[s[l]]:
					have -= 1

				l += 1

		# extract the `res` into two variables named `l` and `r`
		l, r = res

		# Note: We know it's possible that a result does not even exist, so we need to check if resLen is still infinity or not
		return s[l:r+1] if resLen != float("infinity") else ""