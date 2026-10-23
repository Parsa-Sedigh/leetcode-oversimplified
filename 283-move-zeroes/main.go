package problem283

// 1. Bubble the zeros to the end (same idea as bubble sort)
// T: O(n^2)
// M: O(1)
func moveZeroes(nums []int) {
	// Each pass pushes one zero all the way to index k, so nums[k] is final after the pass.
	// That's why the next pass can stop one step earlier.
	for k := len(nums) - 1; k >= 0; k-- {
		i := 0

		for i < k {
			// If the current element is zero, swap it with the next one.
			// Since i also moves right, the same zero keeps getting pushed right until it reaches k.
			// The non-zero element only moves one step left, so the order of non-zeros stays the same.
			if nums[i] == 0 {
				nums[i], nums[i+1] = nums[i+1], nums[i]
			}

			i++
		}
	}
}

// 2. Two pointers: "Fill the next free seat"
// Think of nums as a row of seats where 0 is an empty seat.
// We want every person (non-zero) packed at the front, in the same order.
// T: O(n)
// M: O(1)
func moveZeroes(nums []int) {
	// lastNonZeroIdx is the front-most empty seat: where the NEXT person should sit.
	// Every seat before it is already taken, in the right order.
	lastNonZeroIdx := 0

	// r is you walking down the row, checking every seat once.
	for r := 0; r < len(nums); r++ {
		// If the seat at r is empty, we skip it and keep walking.
		if nums[r] != 0 {
			// Found a person at r: tell them "move up to seat lastNonZeroIdx".
			// Every seat between lastNonZeroIdx and r is one we already walked past and found empty,
			// so the swap moves an empty seat back to r. That's how the empty seats drift to the end.
			// (When lastNonZeroIdx == r, the person is already in the right seat and swaps with themselves.)
			nums[lastNonZeroIdx], nums[r] = nums[r], nums[lastNonZeroIdx]
			lastNonZeroIdx++
		}
	}
}
