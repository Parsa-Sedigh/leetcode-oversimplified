package _69_majority_element

// Hashmap
// T: O(n)
// M: O(n)
func majorityElement(nums []int) int {
	counts := make(map[int]int, len(nums))
	majority := 0

	for _, num := range nums {
		counts[num]++

		if counts[num] > counts[majority] {
			majority = num
		}
	}

	return majority
}
