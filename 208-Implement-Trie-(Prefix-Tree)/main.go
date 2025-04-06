package main

type TrieNode struct {
	children map[string]*TrieNode
	word     bool
}

type Trie struct {
	root *TrieNode
}

func Constructor() Trie {
	return Trie{
		root: &TrieNode{
			children: make(map[string]*TrieNode),
		},
	}
}

func (this *Trie) Insert(word string) {
	cur := this.root

	for _, c := range word {
		node, ok := cur.children[string(c)]

		if !ok {
			node = &TrieNode{
				children: make(map[string]*TrieNode),
			}
		}

		cur.children[string(c)] = node
		cur = cur.children[string(c)]
	}

	cur.word = true
}

func (this *Trie) Search(word string) bool {
	cur := this.root

	for _, c := range word {
		if _, ok := cur.children[string(c)]; !ok {
			return false
		}

		cur = cur.children[string(c)]
	}

	return cur.word
}

func (this *Trie) StartsWith(prefix string) bool {
	cur := this.root

	for _, c := range prefix {
		if _, ok := cur.children[string(c)]; !ok {
			return false
		}

		cur = cur.children[string(c)]
	}

	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
