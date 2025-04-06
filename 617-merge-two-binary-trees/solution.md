### Time and Space
#### # 1. Depth First Search (Creating New Tree)
TIME:

The size of the merged tree varies based on how much the trees overlap in their structure:

- Maximum Overlap (Best Case): If root1 and root2 have identical structures (same shape and node positions), 
the merged tree has the same number of nodes as the larger tree, i.e., max(m,n). For example, two full binary trees with
n nodes each produce a merged tree with n nodes.
- Minimal Overlap (Worst Case): If the trees have completely disjoint structures (e.g., root1 is a left-skewed chain of
  m nodes and root2 is a right-skewed chain of n nodes), the merged tree includes nodes from both, sharing only the root. 
  The total nodes become m + n, and the left and right subtrees are appended.

So in worst case: O(m + n)

SPACE:

- The recursion uses the call stack, with a depth equal to the height of the merged tree.
- In the worst case (skewed trees), this height is O(max(m,n)).
- In balanced trees, it’s `O(max(log(m), log(n)))`. Yeah it's plus because in the callstack we have both 
- Thus, space complexity is O(max(H1, H2)) where H1 and H2 are the heights of root1 and root2.