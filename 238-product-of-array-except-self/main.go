package main

// my solution
// T: O(n)
// M: O(n)
func productExceptSelf(nums []int) []int {
	prefix := make([]int, 0, len(nums))
	suffix := make([]int, 0, len(nums))
	res := make([]int, 0, len(nums))

	for i := 0; i < len(nums); i++ {
		prefix = append(prefix, 1)
		suffix = append(suffix, 1)
		res = append(res, 1)
	}

	total := 1
	for i := 0; i < len(nums); i++ {
		total *= nums[i]
		prefix[i] = total
	}

	total = 1
	for i := len(nums) - 1; i >= 0; i-- {
		total *= nums[i]
		suffix[i] = total
	}

	for i := 0; i < len(nums); i++ {
		pre := 1
		suff := 1

		if i-1 >= 0 {
			pre = prefix[i-1]
		}

		if i+1 < len(nums) {
			suff = suffix[i+1]
		}

		res[i] = pre * suff
	}

	return res
}

// T: O(n)
// M: O(1)
func productExceptSelf2(nums []int) []int {
	res := make([]int, 0, len(nums)) // doesn't count as extra memory since it's the result itself

	for i := 0; i < len(nums); i++ {
		res = append(res, 1)
	}

	prefix := 1
	for i := 0; i < len(nums); i++ {
		res[i] *= prefix
		prefix *= nums[i]
	}

	postfix := 1
	for i := len(nums) - 1; i >= 0; i-- {
		res[i] *= postfix
		postfix *= nums[i]
	}

	return res
}
