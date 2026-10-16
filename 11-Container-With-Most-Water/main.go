package main

// Brute force
// T: O(n^2)
// M: O(1)
func maxArea(height []int) int {
	res := 0

	for l := 0; l < len(height); l++ {
		for r := l + 1; r < len(height); r++ {
			area := (r - l) * min(height[l], height[r])
			res = max(res, area)
		}
	}

	return res
}

// Two pointer
// T: O(n)
// M: O(1)
func maxArea(height []int) int {
	res := 0
	l, r := 0, len(height)-1

	for l < r {
		area := (r - l) * min(height[l], height[r])
		res = max(res, area)

		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}

	return res
}
