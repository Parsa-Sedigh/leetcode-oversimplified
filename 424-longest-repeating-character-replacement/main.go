package main

// T: O(n)
// M: O(26)
func characterReplacement(s string, k int) int {
	count := make(map[byte]int)
	res := 0
	l := 0
	maxF := 0

	for r := 0; r < len(s); r++ {
		count[s[r]] += 1
		maxF = max(maxF, count[s[r]])

		/* shrink the window until it becomes valid. Why having a for loop and moving l possibly multiple times instead of
		just an if block and moving l once? It maybe the case that by moving r one time forward, the whole window becomes invalid and
		we have to move l forward multiple times. Like when having `aaabaaaa` with `k = 0`. The `res` is `4`. Now when we hit b, we have
		to move l all the way to b. So we need a for loop with moving l multiple times not just a single time. */
		for r-l+1-maxF > k {
			count[s[l]] -= 1
			l += 1
		}

		res = max(res, r-l+1)
	}

	return res
}
