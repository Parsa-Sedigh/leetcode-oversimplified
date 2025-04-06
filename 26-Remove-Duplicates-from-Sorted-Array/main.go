package main

// T: O(n)
// M: O(n)
func removeDuplicates1(nums []int) int {
	l := 0
	uniqueItems := make(map[int]struct{})

	for r := 0; r < len(nums); r++ {
		if _, ok := uniqueItems[nums[r]]; !ok {
			nums[l] = nums[r]
			l++
		}

		uniqueItems[nums[r]] = struct{}{}
	}

	return l
}

func removeDuplicates2(nums []int) int {
	l := 1

	for r := 1; r < len(nums); r++ {
		if nums[r-1] != nums[r] {
			nums[l] = nums[r]
			l++
		}
	}

	return l
}
