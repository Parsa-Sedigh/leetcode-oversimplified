package problem278

import "fmt"

func isBadVersion(version int) bool {
	return false
}

func firstBadVersion(n int) int {
	start := 0
	end := n
	minBadVersion := 0

	for start <= end {
		middle := (start + end) / 2
		fmt.Println(middle)

		/* If we find a bad version, it means it could be the first bad version itself or it was one of the earlier ones. So for now,
		the bad version is actually the one we found. But we don't know for sure it was the first one, maybe the another older one was the
		bad version. So we need to still search for it. But we know that after that bad one, all of them are bad, so let's narrow the searching
		by making the end be the one before middle(if we do: end = middle, we would have an infinite for loop)*/
		if isBadVersion(middle) {
			/* If you don't decrement middle and pass it to end, the start and end would never pass from each other and therefore the loop
			would be infinite.*/
			end = middle - 1
			minBadVersion = middle
		} else {
			start = middle + 1
		}

	}

	return minBadVersion
}
