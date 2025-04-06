from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# T: O(n * log(n))
# M: O(log(n)) - since this is recursive solution and the height of the decision tree is log(n).

# SOME QUESTIONS AROUND MEMORY COMPLEXITY IN THIS PROBLEM:
# 1. Why height?
# Because we're dealing with a recursive func, that's why we're thinking in terms of decision tree in the first place, right?
# Now the max depth of the call stack contributes to the worst memory complexity. The max depth here is log(n).

# 2. Now why log(n)?
# Because that's how many times we can divide n by 2 until it becomes 1 - our base case.

# 3. Now why our base case is 1?
# Because having a single node is our base case for sorting.

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases: when there's no node, or only one node, there's nothing to split anymore. We should merge the sub linked lists.
        if not head or not head.next:
            # by returning head and not None, we cover the both base cases.
            return head

        # At each step, left is head and right is middle of LL with head being the head of it. Then we
        # want to split the LL in the middle. To do this, set the next field of `right` to None. So that we have two LL now.
        # But before doing that, we need to save the right half of the LL to avoid losing it.
        left = head
        right = self.getMid(head)

        # since we're gonna set the right.next to None, we have to save the right sub linked list somewhere, so put it in tmp.
        # After setting right.next = None, set `right` back to point to the right half of the LL. Note that right.next
        # is the first el of the right LL. So `right` itself is effectively in the LEFT LL.
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    # T: O(n)
    # M: O(1)
    def getMid(self, head: ListNode) -> ListNode:
        # with slow and fast pointer technique, when fast goes at the end of the LL or out of bounds, slow will
        # always point to the middle node.
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # T: O(n)
    # M: O(1)
    # merge assumes left and right linked lists are already sorted. It's gonna merge these two LLs into one sorted LL.
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        # to avoid edge cases
        tail = dummy = ListNode()

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        # it could be that some of the nodes in left linked list are still not got into the linked list that we've created in this
        # method(the one that it's head is dummy.next). Why? Because left linked list was longer than right.
        # NOTE: only one or none of these two if blocks will run since one of them could be longer than the other.
        # If both are equal, none of these if blocks will execute.
        if left:
            tail.next = left

        if right:
            tail.next = right

        return dummy.next
