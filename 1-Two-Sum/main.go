package main

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
