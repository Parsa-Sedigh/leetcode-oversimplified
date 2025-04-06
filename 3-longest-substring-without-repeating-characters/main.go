package main

/*
	My solution

T: O(n)
M: O(n)
*/
func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 || len(s) == 1 {
		return len(s)
	}

	L := 0
	longest := 0
	items := make(map[string]struct{})

	for R := 0; R < len(s); R++ {
		if _, ok := items[string(s[R])]; ok {

			/* We shouldn't do L = R, because we can possibly skip valid windows. For example consider: "dvdf".
			When we reach the second d, we just need to move L ONE index forward. Otherwise, if we do L = R, we would
			skip the "v" and get incorrect result.*/

			for {
				if _, ok2 := items[string(s[R])]; ok2 {
					/* It's very important to delete s[L] not s[R]. Since we're moving l, so it's respective element must be
					removed from map before moving l forward. But the above if condition is on s[R] not s[L]. Because when there's
					a duplicate of s[R] in curr substring, we move l forward and delete the s[l] until we remove the duplicate.
					Note: We don't need a l <= r for the for condition. Because when l reaches r, the items would be empty and
					the else block would be executed and we break out of the loop. So l couldn't pass r and go out of bounds.*/
					delete(items, string(s[L]))
					L += 1
				} else {
					break
				}
			}
		}

		longest = max(longest, R-L+1)
		items[string(s[R])] = struct{}{}
	}

	return longest
}
