package main

// my solution
// T: O(n)
// M: O(n)
func checkInclusion(s1 string, s2 string) bool {
	s1Map := make(map[string]int)
	s2Map := make(map[string]int)

	for _, s := range s1 {
		s1Map[string(s)]++
	}

	var l int

	for r := range s2 {
		if r-l+1 > len(s1) {
			s2Map[string(s2[l])]--
			l++
		}

		s2Map[string(s2[r])]++

		resLen := 0

		for k1, v1 := range s1Map {
			if v2, ok := s2Map[k1]; ok && v1 == v2 {
				resLen++
			}
		}

		if resLen == len(s1Map) {
			return true
		}
	}

	return false
}
