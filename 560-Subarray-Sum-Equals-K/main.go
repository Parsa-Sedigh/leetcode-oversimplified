package main

// T: O(n^2)
// M: O(1)
func subarraySum(nums []int, k int) int {
	res := 0

	for i := 0; i < len(nums); i++ {
		currSum := 0

		for j := i; j < len(nums); j++ {
			currSum += nums[j]

			if currSum == k {
				res += 1
			}
		}
	}

	return res
}

// T: O(n)
// M: O(n)
func subarraySum2(nums []int, k int) int {

}
