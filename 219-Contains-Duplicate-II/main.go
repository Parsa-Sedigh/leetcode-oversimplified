package main

func containsNearbyDuplicate(nums []int, k int) bool {
	L := 0
	items := make(map[int]struct{})

	for R := 0; R < len(nums); R++ {
		if R-L > k {
			delete(items, nums[L])
			L += 1
		}

		if _, ok := items[nums[R]]; ok {
			return true
		}

		items[nums[R]] = struct{}{}
	}

	return false
}
