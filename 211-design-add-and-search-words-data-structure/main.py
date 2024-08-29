class TrieNode:
    def __init__(self):
        self.children = {} # for example: { a: TrieNode, ... }
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    # T: O(n) - n is len of word

    # M: O(n * 26)
    # Why? Because we have n nodes and each node can have up to 26 children. The actual space used depends on the
    # number of unique prefixes in all the words added.
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.word = True

    # T: O(n * (26 ^ k)) - where n is len of word and k is number of "." in the word.
    # Why 26 to the power of k? Because when we encounter a ".", at worst case we could have 26 children at each step.
    # So in worst case, at each step, the number of nodes of the tree gonna be 26 times more, hence 26^k.
    # M: O(n) - where n is len of word
    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            # for every char of the current remainings of `word`:
            for i in range(j, len(word)):
                c = word[i]

                # if current char is a ".", it means potentially we're gonna go 26 different paths until we find the word. So we use
                # backtracking(recursion).
                if c == ".":
                    for child in cur.children.values():
                        # if at any step, we found the word, return to the caller(parent)
                        if dfs(i + 1, child):
                            return True

                    # nothing was found by searching on all children, so return false
                    return False
                else:
                    if c not in cur.children:
                        return False

                    cur = cur.children[c]

            return cur.word

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)