package main

// assuming s and t are the same size n:
// T: O(n)
// M: O(n)
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	sMap := make(map[rune]int)
	tMap := make(map[rune]int)

	for _, c := range s {
		sMap[c] += 1
	}

	for _, c := range t {
		tMap[c] += 1
	}

	for k := range sMap {
		if sMap[k] != tMap[k] {
			return false
		}
	}

	return true
}
