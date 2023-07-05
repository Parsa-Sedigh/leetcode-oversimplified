import math
from typing import List


class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		l, r = 1, max(piles)

		# Since we're looking for k in the minimum number of hours with the speed of k, initially set result to be the maximum possible
		# value of a pile. Because we know this value will definitely work. But we possibly need to find smaller values to find the minimum.
		res = r

		while l <=r:
			k = (l + r) // 2

			# for current k, how many hours does it take to eat all bananas?
			hours = 0

			for p in piles:
				hours += math.ceil(p / k)

			# it means we can update our result because our current hours is less than the required hour
			if hours <= h:
				res = min(res, k)

				# let's look for an even smaller k, so set right pointer to k - 1(we wanna search the left portion now)
				r = k - 1

			# if we got into else, that means the speed was too small for eating all bananas in required h, so we need to find a bigger speed
			else:
				l = k  + 1

		return res

