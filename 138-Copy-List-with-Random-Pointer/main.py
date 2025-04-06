# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# T: O(n)
# M: O(n)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # maps every old node to it's copy that we create
        oldToCopy = {None: None}
        cur = head

        # in this pass, we create a hashmap of old to copy.
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head

        # set the pointers
        while cur:
            copy = oldToCopy[cur]

            # What if cur.next is null? Well in this case we want the result of oldToCopy[cur.next] to be None. Essentially
            # here, we have this: oldToCopy[None], which must return None. So in the hashmap, set this mapping: {None: None}.
            # Note: In other words, if we have a old node that's None, we want the copy to be None as well.
            # Note: Here, we want the respective copy of `cur.next` which is `oldToCopy[cur.next]`
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        # oldToCopy[head] gives us the head of the copy nodes LL
        return oldToCopy[head]

# T: O(n)
# M: O(1)
# Note: The new nodes are part of the deep copy and do not count as extra space since they are part of the required OUTPUT.
class Solution2:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head

        # Step 1: Create new nodes and insert them after original nodes
        while cur:
            new_node = Node(cur.val, cur.next)
            cur.next = new_node
            cur = new_node.next

        # Step 2: Assign the Random pointers
        cur = head
        while cur:
            # if cur.random is not None, it means we arrived at an original node. So it's next node is a copied one.
            # We know cur.random points to the original node's random node. cur.random.next is the copy of that random node.
            # We wanna point the original node's copy random field(`cur.next.random`), to original node's random copy. This way the copy and
            # it's random counterpart are matched. The original node's random lives at `cur.random` and it's copy lives at: `cur.random.next`
            if cur.random:
                cur.next.random = cur.random.next

            # the next original pointer is at cur.next.next
            cur = cur.next.next

        # Step 3: Separate the original and copied lists
        cur = head

        # new_head is the next node of our original head
        new_head = head.next
        new_cur = new_head

        while cur:
            cur.next = new_cur.next
            cur = cur.next

            if cur:
                new_cur.next = cur.next
                new_cur = new_cur.next

        return new_head