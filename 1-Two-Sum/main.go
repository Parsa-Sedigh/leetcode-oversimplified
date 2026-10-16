package main

import (
	"slices"
)

// Brute force
// T: O(n^2)
// M: O(1)
func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}

	return nil
}

// Hash Map
// T: O(n)
// M: O(n)
func twoSum(nums []int, target int) []int {
	items := make(map[int]int)

	for i, num := range nums {
		if index, ok := items[target-num]; ok {
			return []int{i, index}
		}

		items[num] = i
	}

	return []int{}
}

// sorting
// T: O(n * log(n))
// M: O(n)
func twoSum(nums []int, target int) []int {
	type pair struct {
		index int
		value int
	}

	originalNums := make([][2]int, 0, len(nums))
	for i, num := range nums {
		originalNums = append(originalNums, [2]int{i, num}) // originalNums = [[0, 3], [1, 2], [2, 4]]
	}

	slices.SortFunc(originalNums, func(a, b [2]int) int {
		return a[1] - b[1]
	})

	l, r := 0, len(nums)-1
	for l < r {
		sum := originalNums[l][1] + originalNums[r][1]
		if sum < target {
			l++
		} else if sum > target {
			r--
		} else {
			return []int{originalNums[l][0], originalNums[r][0]}
		}
	}

	return nil
}
