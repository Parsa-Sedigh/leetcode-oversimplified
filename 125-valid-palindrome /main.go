package problem125

import (
	"fmt"
	"strings"
	"unicode"
)

func isPalindrome(s string) bool {

	l := 0
	r := len(s) - 1
	for l < r {
		fmt.Println("l: ", string(s[l]), "r: ", string(s[r]))

		if unicode.IsLetter(rune(s[l])) && unicode.IsLetter(rune(s[r])) &&
			strings.ToLower(string(s[l])) != strings.ToLower(string(s[r])) {

			return false
		}

		l++
		r--
	}

	return true
}
