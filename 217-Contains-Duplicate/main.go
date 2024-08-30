package main

import "slices"

// T: O(n)
// M: O(n)
func containsDuplicate(nums []int) bool {
	visited := make(map[int]struct{})

	for i := 0; i < len(nums); i++ {
		if _, ok := visited[nums[i]]; ok {
			return true
		}

		visited[nums[i]] = struct{}{}
	}

	return false
}

// T: O(n * log(n))
// M: O(1)
// The slices.Sort(nums) function sorts the array in place, so it doesn't require additional space proportional to
// the input size, aside from a small amount of stack space for the sorting algorithm (e.g., quicksort typically requires
// O(log n) space for recursion).
func containsDuplicate2(nums []int) bool {
	slices.Sort(nums)

	for i := 1; i < len(nums); i++ {
		if nums[i-1] == nums[i] {
			return true
		}
	}

	return false
}
