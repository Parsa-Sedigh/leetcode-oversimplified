package problem125

import (
	"strings"
	"unicode/utf8"
)

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
