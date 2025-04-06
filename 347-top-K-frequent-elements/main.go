package main

func topKFrequent(nums []int, k int) []int {
	count := make(map[int]int)

	for _, num := range nums {
		count[num]++
	}

	freq := make([][]int, len(nums)+1)

	for num, f := range count {
		freq[f] = append(freq[f], num)
	}

	var res []int
	for i := len(freq) - 1; i >= 0; i-- {
		res = append(res, freq[i]...)

		if len(res) == k {
			return res
		}
	}

	// the prev `return` is guaranteed to execute at some point. So we would never reach this line, hence we return empty slice.
	return []int{}
}
