Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

A: The fixed-size array approach uses an array of 26 elements, relying on `ord(char) - ord('a')` to map lowercase letters to
indices 0–25. This won't work for Unicode, as there are potentially millions of unique characters (Unicode supports over 1.1 million code points).
Instead, use the hashmap approach.