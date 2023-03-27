package search_insert_position

func searchInsert(nums []int, target int) int {
	start := 0
	end := len(nums) - 1

	for start <= end {
		middle := (start + end) / 2

		if nums[middle] == target {
			return middle
		} else if nums[middle] < target {
			start = middle + 1
		} else {
			end = middle - 1
		}
	}

	return start
}
