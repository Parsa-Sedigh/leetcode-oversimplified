package main

import (
	"math"
)

// my solution
// T: O(n).
/* Note: Why time is O(n) and not O(n^2)?
Because if the inner loop ran for each iteration of the outer loop, the complexity would indeed be O(n^2).
However, in this algorithm, the inner loop does not run independently for each outer loop iteration.
The L pointer advances only when necessary, ensuring that the total number of operations remains linear.*/
// M: O(1)
func minSubArrayLen(target int, nums []int) int {
	L := 0
	minLen := math.MaxInt
	currSum := 0
	gotRes := false

	for R := 0; R < len(nums); R++ {
		currSum += nums[R]

		for currSum >= target {
			gotRes = true
			minLen = min(minLen, R-L+1)

			currSum -= nums[L]
			L += 1
		}
	}

	if gotRes {
		return minLen
	}

	return 0
}
