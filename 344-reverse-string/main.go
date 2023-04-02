package problem344

func reverseString(s []byte) {
	start := 0
	end := len(s) - 1

	for start <= end {
		tmp := s[end]
		s[end] = s[start]
		s[start] = tmp

		start++
		end--
	}
}
