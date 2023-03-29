package problem977

import "sort"

func sortedSquares(nums []int) []int {
	l := 0
	r := len(nums) - 1
	var res []int

	for l <= r {
		lSquared := nums[l] * nums[l]
		rSquared := nums[r] * nums[r]

		if lSquared >= rSquared {
			res = append(res, lSquared)

			// we appended the left one, so we don't need to worry about it, therefore increment l to compare the next one
			l++
		} else {
			res = append(res, rSquared)
			r--
		}
	}

	sort.Ints(res)

	return res
}
