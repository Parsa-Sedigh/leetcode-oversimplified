package main

type TrieNode struct {
	children map[rune]*TrieNode
	word     bool
}

type WordDictionary struct {
	root *TrieNode
}

func Constructor() WordDictionary {
	return WordDictionary{
		root: &TrieNode{
			children: make(map[rune]*TrieNode),
		},
	}
}

func (this *WordDictionary) AddWord(word string) {
	cur := this.root

	for _, c := range word {
		if _, ok := cur.children[c]; !ok {
			cur.children[c] = &TrieNode{
				children: make(map[rune]*TrieNode),
			}
		}

		cur = cur.children[c]
	}

	cur.word = true
}

func (this *WordDictionary) Search(word string) bool {
	return dfs(this.root, word, 0)
}

func dfs(root *TrieNode, word string, index int) bool {
	cur := root

	// can't use a range loop here and we can't subslice the word here.
	for i := index; i < len(word); i++ {
		c := rune(word[i])

		if c == '.' {
			for _, child := range cur.children {
				if dfs(child, word, i+1) {
					return true
				}
			}

			return false
		} else {
			if _, ok := cur.children[c]; !ok {
				return false
			}

			cur = cur.children[c]
		}
	}

	return cur.word
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */

/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */
