The arrays represented as the tree structures in the description are not real. They're generated by leetcode website itself. We can'
use them. The actual p and q are a tree DS not an array. So don't be super smart and say: Yeah, p and q are arrays so let's just compare the
length of p and q and their elements. This won't work because p and q are not arrays, but trees, leetcode is just showing them like that.

Time complexity: `O(p + q)` - it's size of the both trees added together, because worst case, we would have to iterate through every
single node in both trees

Space complexity: `O(p + q)`