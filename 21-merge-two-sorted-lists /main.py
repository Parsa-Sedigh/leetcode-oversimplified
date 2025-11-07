class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. Recursion
# T: O(n + m)
# M: O(1)

# n: len of l1
# m: len of l2

# NOTE: Pick the smaller head, then recurse on the rest
# At each step:
# - Compare the first nodes of both lists.
# - The smaller one becomes the next node in the result.
# - Then recursively merge the rest.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Base case 1
        if not l1:
            return l2

        # Base case 2
        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)

            # since l1 is less than l2, l1 should be returned to the parent(prev node)
            return l1

        l2.next = self.mergeTwoLists(l1, l2.next)

        return l2


# 2. Iteration

# T: O(n + m)
# M: O(1)

# n: len of l1
# m: len of l2
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # dummy holds the entire result list(which means it points to the head of the result list). We need another pointer for traversing
        # the result linked list. So we create another variable called tail and initially point it to the head of the result linked list
        # Note that we never update the dummy or move it. Because it should hold the list. Instead we use a helper variable for
        # adding new nodes.
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            # take the remaining portion of l1 and add it to the end of the result list which is pointed by the tail variable
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next
