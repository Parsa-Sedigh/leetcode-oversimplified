from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


# The reason we didn't define a search() method is because we're gonna be doing that simultaneously as we do our dfs on the board.
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.word = True


# Brute force
# T: O(w * m * n * 4^(m * n)) - where w is number of words and m is number of cols and n number of rows
# Note: One dfs() for a single cell, will take 4^(m*n). Now since we're doing it for all cells of the grid, it will
# take: m * n * 4^(m * n). Now we do this operation for every word in the words list, so overall is: O(w * m * n * 4^(m * n))
# where w is length of the words list.

# M: O(m * n)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        res = []

        def dfs(r, c, curr):
            if (min(r, c) < 0 or
                    r == ROWS or c == COLS or
                    (r, c) in visit):
                return

            visit.add((r, c))
            curr += board[r][c]

            # T: O(k) - where k is number of words in the `words` list
            if curr in words and curr not in res:
                res.append(curr)

            dfs(r + 1, c, curr)  # move down
            dfs(r - 1, c, curr)  # move up
            dfs(r, c + 1, curr)  # move right
            dfs(r, c - 1, curr)  # move left

            visit.remove((r, c))

        for _ in words:
            for r in range(ROWS):
                for c in range(COLS):
                    dfs(r, c, "")

        return res


class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for w in words:
            trie.add_word(w)

        ROWS, COLS = len(board), len(board[0])

        # Note: It's possible that we visit the same word twice inside of our board but we don't want to have duplicates in the `res`,
        # therefore we use a hashset as res.
        # Note: We use a hashset for the cells that we've visited, because we don't wanna get into an infinite loop and we don't want
        # to repeat the same char more than once because we're not allowed to.
        res, visit = set(), set()

        # `word` is what word we have so far.
        def dfs(r, c, trie_node: TrieNode, word):
            # if board[r][c] not in trie_node.children is true it means this char is not the next char of any `words`,
            # so we can't move forward this path anymore.
            if (r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    (r, c) in visit or
                    board[r][c] not in trie_node.children):
                return

            visit.add((r, c))
            trie_node = trie_node.children[board[r][c]]
            word += board[r][c]

            if trie_node.word:
                res.add(word)

            # go into each 4 directions from current cell
            dfs(r - 1, c, trie_node, word)
            dfs(r + 1, c, trie_node, word)
            dfs(r, c - 1, trie_node, word)
            dfs(r, c + 1, trie_node, word)

            # we are backtracking and visit is a reference type, meaning it doesn't reset by itself in each recursive call,
            # so we have to reset it ourselves in the backtrack step:
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                # when we wanna start dfs at each cell, we know we wanna find a word that is in our trie. The words all start
                # from the root of the trie, so we pass the root of the trie as the starting point of search in our trie.
                dfs(r, c, trie.root, "")

        return list(res)