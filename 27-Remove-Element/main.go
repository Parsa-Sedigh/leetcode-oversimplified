package main

func removeElement(nums []int, val int) int {
	if len(nums) == 0 {
		return 0
	}

	l, r := 0, len(nums)-1

	for i := len(nums) - 1; i >= 0; i-- {
		if nums[i] != val {
			break
		}

		if nums[i] == val {
			r = i
		}
	}

	for l <= r {
		if nums[l] == val {
			tmp := nums[l]
			nums[l] = nums[r]
			nums[r] = tmp

			r--
		} else {
			l++
		}
	}

	return l
}
