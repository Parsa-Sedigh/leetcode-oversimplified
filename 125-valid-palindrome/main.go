package main

import (
	"strings"
	"unicode/utf8"
)

// T: O(n)
/* The main loop iterates through the string once, with each character processed at most twice (once by l and once by r).
Therefore, the time complexity is O(n), where n is the length of the string s.
The inner loops (within the main loop) also iterate AT MOST n times in total, so they don't increase the overall time complexity.
Note: They run AT MOST n times and not n times in each iteration of outer loop. So inner loops don't make time O(n^2).
The strings.ToLower function has a complexity of O(1) since it is operating on a single character.
*/

// M: O(1)
func isAlphaNum(r rune) bool {
	ACodePoint, _ := utf8.DecodeRuneInString("A")
	ZCodePoint, _ := utf8.DecodeRuneInString("Z")
	aCodePoint, _ := utf8.DecodeRuneInString("a")
	zCodePoint, _ := utf8.DecodeRuneInString("z")
	zeroCodePoint, _ := utf8.DecodeRuneInString("0")
	nineCodePoint, _ := utf8.DecodeRuneInString("9")

	return (ACodePoint <= r && r <= ZCodePoint) ||
		(aCodePoint <= r && r <= zCodePoint) ||
		(zeroCodePoint <= r && r <= nineCodePoint)
}

func isPalindrome(s string) bool {
	l := 0
	r := len(s) - 1

	for l < r {

		for l < r && !isAlphaNum(rune(s[l])) {
			l++
		}

		for r > l && !isAlphaNum(rune(s[r])) {
			r--
		}

		if strings.ToLower(string(s[l])) != strings.ToLower(string(s[r])) {
			return false
		}

		l++
		r--
	}

	return true
}
