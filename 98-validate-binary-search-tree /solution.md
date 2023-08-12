Valid BST:
- **every single node** in the left subtree is going to be less((not less than or equal, strictly less) than the current node
- every single node in the right subtree are going to be greater(not greater or equal, strictly greater) than the current node

We need a DFS to solve this.

Q: Is [5, 3, 7, null, null, 4, 8] a binary search tree?

A: No(though it's easy to miss the correct answer). 4 is in the right subtree, but it's less than the root(5).

Note: An incorrect solution would be just to check the neighbors and this won't work because of the previous question.

---

### Brute force approach:

For every node, check every value in the left subtree, make sure every value is less than the current node and then check every value in the right subtree
and make sure they're greater than the current node. So for every node we would have n comparisons, so O(n) and we have to repeat this process
for every subtree which is gonna be O(n). So the time complexity overall is `O(n^2)`.

Space complexity: O(h)

---

### Better approach:
The root of the tree be any value, there are no restrictions on what the value can be, because it doesn't have any parents. So we can say
it's value can be any value between -Infinity and +Infinity.

We're gonna have 2 boundaries: left and right boundaries.

Note: In our base case of our DFS in this case(`if not root:`), we need to return true because technically **an empty BST is
still a BST.**

- The left boundary indicates the upper limit that a subtree can have. When we go to the left, we know we can't have a value more than the
upper boundary. Therefore we update the right boundary to the current node's value.
- The right boundary indicates the bottom limit that a subtree can have.

**When we go to left subtree:**

When we're going left, we can leave the left boundary as it is, but we're gonna update the right boundary to the current node's value because
we know that a left subtree has to be less than the parent(node.val). So the parent's val is gonna set to the right boundary because we need to make
sure that the left subtree is always less than that right boundary.

**When we go to right subtree:**

The left boundary is going to be updated to the parent's value because the right subtree needs to be greater than the parent's value.
The right boundary is going to stay the same because there is no limit to how much a right subtree can be greater in terms of value.

With this algorithm since for each node all we're doing is making two comparisons only, time complexity is O(2n)