package main

import "sort"

func threeSum(nums []int) [][]int {
	var result [][]int

	sort.Ints(nums)

	for i, num := range nums {
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
				result = append(result, []int{num, nums[l], nums[r]})
				l++

				for nums[l] == nums[l-1] && l < r {
					l++
				}
			}
		}
	}

	return result
}
