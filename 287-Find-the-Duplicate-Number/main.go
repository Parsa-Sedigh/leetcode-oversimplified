package main

import "sort"

// sorting is not allowed per description, just a demonstration.
// T: O(n * log(n))
// M: O(1)
func findDuplicate(nums []int) int {
	// T: O(n * log(n))
	sort.Ints(nums)

	prev := nums[0]

	// T: O(n)
	for _, n := range nums[1:] {
		if prev == n {
			return n
		}

		prev = n
	}

	return 0
}

// floyd's algo
// T: O(n)
// M: O(1)
func findDuplicate2(nums []int) int {

}
