This is a combinations problem.

We wanna use a backtracking template. We want to look at this as a tree.

Look at the decision tree. When we hit the base case at the most left path, we go back up by popping d from the slate and then
pushing e. Then we would hit the base case and therefore we pop e and then push f. Then we hit the base case, pop the f and then there
are no more letters to push. Therefore pop a and go to the second path of root.

We're doing preorder DFS.

Time: Worst case is with 9 and 7. So we could have 4 letters. So 4^n and this is gonna be how many levels of the tree that we're gonna have(based
on the number of characters that the digit is mapped). At the bottom(leaf level) we're gonna do a linear scan , so: `*n`. Therefore: `O(4^n * n)`

Space: `O(4^n * n)`