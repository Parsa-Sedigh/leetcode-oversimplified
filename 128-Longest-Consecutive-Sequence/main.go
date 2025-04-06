package main

// T: O()
// M: O(n)
func longestConsecutive(nums []int) int {
	count := make(map[int]struct{})
	res := 0

	// Add all numbers to the map
	for _, num := range nums {
		count[num] = struct{}{}
	}

	// T: O(n)
	/* This is where the issue lies. For each number that you identify as the start of a sequence, you keep
	incrementing currNum and check whether it exists in count. This can be fine for the first number in a sequence but becomes
	redundant and costly when there are many sequences to check. Since this inner loop runs in O(L) time (where L is the length of the sequence),
	in the worst-case scenario, this can end up being O(n) for each iteration of the outer loop, leading to O(n^2) time complexity overall.

	To avoid O(n^2), we skip the inner loop if num is not start of a seq.*/

	// Check each number if it's the start of a sequence
	for num := range count {
		// If num-1 is not in the map, then num is the start of a sequence. Only start inner loop if num is start of a seq.
		// If we don't use this if statement, we would get: Time limit exceeded
		if _, ok := count[num-1]; !ok {
			// we could avoid using this var and use num + currLen in: `_, ok := count[currNum+1]` line, look at python solution.
			currNum := num
			currLen := 1

			// Check the length of the sequence starting from num
			for {
				_, ok := count[currNum+1]
				if !ok {
					break
				}

				currNum++
				currLen++
			}

			res = max(res, currLen)
		}
	}

	return res
}
