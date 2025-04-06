package main

// brute-force
// T: O(n^2)
// M: O(1)
func twoSum(numbers []int, target int) []int {
	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			result := numbers[i] + numbers[j]

			if result > target {
				break
			} else if result == target {
				return []int{i + 1, j + 1}
			}
		}
	}

	return []int{}
}

// two-pointer
// T: O(n)
// M: O(1)
func twoSum2(numbers []int, target int) []int {
	l, r := 0, len(numbers)-1

	for l < r {
		result := numbers[l] + numbers[r]

		if result > target {
			r--
		} else if result < target {
			l++
		} else {
			return []int{l + 1, r + 1}
		}
	}

	return []int{}
}
