We have to somehow search for the prefix and suffix in one go. So we put all the possible suffixes at the beginning.

For each word, the solution creates a special combination of the suffix and the prefix, separated by a # symbol.
This allows the Trie to handle both the prefix and suffix at the same time in a single traversal.

For each word, the solution appends the word to itself, with a # in the middle: `word + "#" + word`.
This allows the Trie to store all possible rotations of the word's prefix and suffix combinations.
First we put the suffix at the beginning and then a # and then the whole word. Therefore, we can query the suffix and 
prefix in one go.