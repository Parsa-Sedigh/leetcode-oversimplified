import heapq
from typing import List


class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		# Put all of the stones into a max heap. Python does not have a max heap, so we're gonne put them into a min heap but we're gonna
		# multiply every one of these values by -1 .
		stones = [-s for s in stones]

		heapq.heapify(stones) # O(n) operation

		# If we have one stone or zero stones, that's where we can stop, but until then, we take the two largest stones and smash them
		while len(stones) > 1:
			first = heapq.heappop(stones) # first largest
			second = heapq.heappop(stones) # second largest

			# If the stones were equal, we don't need to do anything, because they were just removed from the heap. But if the second
			# stone we popped was less than first stone we popped, we push back the subtraction of them back to the max heap.
			# Note: Why I said the second stone was less than first? Because the second stone is gonna have a smaller or equal weight to
			# the first one. Because in a max heap, the first one is gonna be the heaviest stone(maximum).

			# BUT REMEMBER: We made all the weights negative to simulate a max heap using a min heap. So we have to do: first - second.
			# Why? For example: first = -8, second = -7. If the math is not straightforward, before the next line, you can convert the
			# first and second values to their absolute values using abs() .

			# So second - first is the weight we wanna add. But remember in our heap, we're keeping track of negative values, so we would
			# have to multiply the result by -1.
			if second > first:
				heapq.heappush(stones, (second - first) * -1) # or first - second

		stones.append(0)

		# Since we have negative values in the max heap, we want to return the absolute value.
		return abs(stones[0])
