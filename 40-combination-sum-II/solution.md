If we wanted to get **all** possible combinations, that's pretty easy. It's just going to be a decision tree. For each value,
we could say: 1. include that value 2. or don't include it

Note: No matter how we get the unique combinations, since we do actually have to create all the combinations, the time complexity
overall is: `O(2^n)`. Because that's how many combinations we can have. For each value we can choose to include or not include it.

**Note:** Since all of the numbers of the input array are positive, if at each step we got to a sum that is greater than `target`, we shouldn't
continue it.

The main idea: The left subtree includes the current value but the right subtree doesn't include it. Therefore, the left subtree path is
always going to be different than the right subtree(it's always going to lead to different combinations).

**Note:** We sort the array because if we want to skip some of the elements, we can perfectly do so without skipping potential combinations.

**Note:** Once we get to a combination that sums up to the target, we don't want to continue anymore because all of the input array elements
are positive and if we add positive values, the sum will **always** gonna exceed the target. So we don't continue anymore in that case.