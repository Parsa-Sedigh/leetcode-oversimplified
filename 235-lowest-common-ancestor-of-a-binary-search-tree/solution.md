We're gonna start at the root of the tree, because the root is always gonna be a common ancestor of every single node in the tree. But
it's not necessary the **lowest** common ancestor, but it is a common ancestor.

With our approach, we don't have to visit every single node in the entire tree, so:

note: We don't need to put any return statements outside of the loop because we're guaranteed that the `else` block is gonna execute at some point
and we return the result there.

Time complexity: O(logn) - because we only gonna have to visit one node for every single level in the tree. So the time complexity is the
height of the tree which usually is gonna be `logn`, unless the tree is inbalanced which in that case, it's gonna be `O(h)`.

Space complexity: O(1)