package main

// my solution
// T: O(n)
// M: O(n)
func pivotIndex(nums []int) int {
	leftPrefixSum := make([]int, 0, len(nums))
	rightPrefixSum := make([]int, 0, len(nums))

	for i := 0; i < len(nums); i++ {
		leftPrefixSum = append(leftPrefixSum, 0)
		rightPrefixSum = append(rightPrefixSum, 0)
	}

	prefix := 0

	for i := 1; i < len(nums); i++ {
		prefix += nums[i-1]
		leftPrefixSum[i] = prefix
	}

	prefix = 0

	for i := len(nums) - 2; i >= 0; i-- {
		prefix += nums[i+1]
		rightPrefixSum[i] = prefix
	}

	for i := 0; i < len(nums); i++ {
		if leftPrefixSum[i] == rightPrefixSum[i] {
			return i
		}
	}

	return -1
}
