package main

import "sort"

// Idea: sort, pick the first number, then find the other two with two pointers.
// T: O(n^2)
// M: O(1) extra, not counting the sort and the output. But if we consider the output as well, it's O(n^2) since We need to
// store all distinct triplets that sum to 0, which can be at most O(n²) triplets.
//
// Easy-to-miss mistakes:
//  1. Save VALUES, not indexes: nums[l], not l.
//  2. Skip a repeated first number with `if`, not `for`.
//     Inside a `for`, `continue` restarts that same small loop, so it never ends.
//  3. Compare with the number BEFORE: nums[i] == nums[i-1].
//     Comparing with nums[i+1] skips the first -1 and loses [-1, -1, 2].
//  4. After a match, move l AND r to NEW values (l++, r--, then skip repeats on both).
//     If they keep the same values, the sum is 0 again and you save the same triplet twice.
//     (Skipping repeats on just one side also works. Skipping on both makes the two sides look the same.)
//  5. Each pointer compares with the value it just LEFT: l with nums[l-1], r with nums[r+1].
//     Writing nums[r-1] skips a value not used yet: [-4, 0, 2, 2, 4] loses [-4, 2, 2].
//  6. Bounds check first: `l < r && nums[l] == nums[l-1]`, never the other way round.

// Version 1: the two-pointer part in its own function.
func threeSum(nums []int) [][]int {
	sort.Ints(nums)

	var result [][]int
	for i := 0; i < len(nums); i++ {
		// `if`, not `for` (mistake 2). Look BACK at i-1 (mistake 3).
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		res := twoSumAfterIdx(nums, i)
		result = append(result, res...)
	}

	return result
}

// twoSumAfterIdx finds every pair after index idx that adds up to -nums[idx].
func twoSumAfterIdx(nums []int, idx int) [][]int {
	var result [][]int

	l, r := idx+1, len(nums)-1
	for l < r {
		sum := nums[idx] + nums[l] + nums[r]

		if sum < 0 {
			l++
		} else if sum > 0 {
			r--
		} else {
			// Values, not indexes (mistake 1).
			result = append(result, []int{nums[idx], nums[l], nums[r]})
			l++
			r--

			// Move l and r to new values, or this triplet is saved again (mistake 4).
			// Compare with the value just LEFT: l-1 and r+1 (mistake 5).
			for l < r && nums[l] == nums[l-1] {
				l++
			}
			for l < r && nums[r] == nums[r+1] {
				r--
			}
		}
	}

	return result
}

// Version 2: everything in one function.
func threeSum(nums []int) [][]int {
	var result [][]int

	sort.Ints(nums)

	for i, num := range nums {
		// `if`, not `for` (mistake 2). Look BACK at i-1 (mistake 3).
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		l, r := i+1, len(nums)-1

		for l < r {
			res := num + nums[l] + nums[r]

			if res > 0 {
				r--
			} else if res < 0 {
				l++
			} else {
				// Values, not indexes (mistake 1).
				result = append(result, []int{num, nums[l], nums[r]})
				l++
				r--

				// Move l and r to new values (mistake 4). Compare with l-1 and r+1 (mistake 5).
				// Bounds check first (mistake 6).
				for l < r && nums[l] == nums[l-1] {
					l++
				}
				for l < r && nums[r] == nums[r+1] {
					r--
				}
			}
		}
	}

	return result
}
