from typing import List, Optional

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # T: O(L) - where L is length of the word
    # M: O(L)
    def add_word(self, i: int, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]
            cur.children["$"] = i

        cur.word = True

    # T: O(L)
    # M: O(1)
    def starts_with(self, word: str) -> Optional[TrieNode]:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return None

            cur = cur.children[c]

        return cur

class WordFilter:

    # T: O(n * L ^ 2) - where n is number of words and L is average length of a word
    # Note: For n words, each of length `L`, you're adding `L` rotations, each taking `O(L)` time to insert(add_word() method).

    # M: O(n * L) - not O(n * L^2)
    # To calculate space complexity, we have to see how many nodes exist? There are n words and each word has
    # TOTAL(not at each iteration) of L rotations and each word is of size L.
    def __init__(self, words: List[str]):
        self.trie = Trie()

        # T: O(n)
        for idx, word in enumerate(words):
            word += "#"
            length = len(word)
            word += word

            # T: O(L)
            for i in range(length):
                cur = self.trie.root
                cur.children["$"] = idx

                # T: O(L)
                self.trie.add_word(idx, word[i:])

    # T: O(L). traversing a string of length `L + L + 1 = 2L + 1` at most => O(L)
    # M: O(1)
    def f(self, pref: str, suff: str) -> int:
        cur = self.trie.root

        for c in f"{suff}#{pref}":
            if c not in cur.children:
                return -1

            cur = cur.children[c]

        return cur.children["$"]



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)