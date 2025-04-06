package main

// my solution
func numOfSubarrays(arr []int, k int, threshold int) int {
	res := 0
	L := 0

	for R := 0; R < len(arr); R++ {
		currLen := R - L + 1

		if currLen > k {
			L += 1
			currLen -= 1
		}

		if currLen == k {
			var sum int
			for _, el := range arr[L : R+1] {
				sum += el
			}

			avg := sum / currLen

			if avg >= threshold {
				res += 1
			}
		}
	}

	return res
}
