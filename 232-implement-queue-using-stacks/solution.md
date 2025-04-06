## Time complexity of pop() and peek()
If s2 is empty, all elements from s1 are moved to s2 by popping from s1 and appending to s2. This takes O(n) time in
the worst case, where n is the number of elements in s1.
**HOWEVER**, this cost is **amortized over multiple pop operations**. Each element is moved from s1 to s2 at most once per push operation.
After moving elements (if necessary), the top element from s2 is popped, which is O(1).

Time Complexity: Amortized O(1)