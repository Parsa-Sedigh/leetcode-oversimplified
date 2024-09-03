## Brute force
For every single word in the list of `words`, go through every single cell and start a DFS from there. 
So using brute-force, we're gonna check what word we can come up with starting from that cell?

Note: We can construct multiple words starting from a cell, so we can't stop after finding a word. We gotta go through whole
cells starting from every single cell.

## trie
With this solution, we can get rid of 2 w in time complexity of prev solution. So we would have: `T: O(m * n * 4^(m * n))`
We only have to run dfs starting from each position, a single time. Because at every cell, we're gonna get all the words
that can be created from that cell.

So instead of just checking a single word at a time, in other words, running dfs on every cell just to check if current word exists
starting from that cell, we can instead simultaneously check **all the words** in `words` that can be created from current cell.
We can find all words starting from current cell based on a prefix. We use trie(prefix tree).

As we move forward in dfs, we see which `words` can still be constructed given the current prefix?
But we don't want to go through the list of `words` at each step. Instead, first create the prefix tree of `words`,
then we wanna check the current prefix in the constructed trie.

![](212-1.png)