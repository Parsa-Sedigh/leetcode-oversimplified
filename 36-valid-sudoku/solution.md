For each rule we can use a hash set(dictionary). Since we know the dimensions of the soduku board, you could use arrays as well.

The third rule is a bit more tricky.

Time complexity: O(9^2) - so O(n)

Space(memory) complexity: O(9^2) - so O(n) , because we're gonna have 3 hash sets which are gonna be exact size of 81 elements.

`(r // 3, c // 3)` tells us the current square that we're in.

**Invalid** board example:

```
[
    [".",".",".",   ".","5",".",    ".","1","."],
    [".","4",".",   "3",".",".",    ".",".","."],
    [".",".",".",   ".",".","3",    ".",".","1"],

    ["8",".",".",   ".",".",".",    ".","2","."],
    [".",".","2",   ".","7",".",    ".",".","."],
    [".","1","5",   ".",".",".",    ".",".","."],

    [".",".",".",   ".",".","2",    ".",".","."],
    [".","2",".",   "9",".",".",    ".",".","."],
    [".",".","4",   ".",".",".",    ".",".","."]
]
```