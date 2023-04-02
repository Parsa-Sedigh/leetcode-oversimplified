package problem557

import (
	"strings"
)

func reverseWords(s string) string {
	slice := strings.Split(s, " ")
	var answer []string

	for _, word := range slice {
		wordByte := []byte(word)
		start := 0
		end := len(wordByte) - 1

		for start <= end {
			tmp := wordByte[end]
			wordByte[end] = wordByte[start]
			wordByte[start] = tmp

			start++
			end--
		}

		answer = append(answer, string(wordByte))
	}

	return strings.Join(answer, " ")
}
