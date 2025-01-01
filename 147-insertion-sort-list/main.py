from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# T: O(n^2) - just like insertion sort
# M: O(1)
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # we could use only one pointer here as well. But using two pointers, make the code a bit cleaner.
        prev, cur = head, head.next

        while cur:
            if cur.val >= prev.val:
                prev, cur = prev.next, cur.next

                continue

            tmp = dummy

            while cur.val > tmp.next.val:
                tmp = tmp.next

            # NOTE: now cur is not larger than the el after tmp. So cur should be placed between tmp and tmp.next . It's the correct spot for cur.
            # So remove cur from where it lives right now and place it between tmp and tmp.next .
            # Note: To remove cur, do: prev.next = cur.next
            prev.next = cur.next

            # NOTE: We can't do tmp.next = cur AND THEN cur.next = tmp.next because the order of these two lines is important and it's wrong here.
            # Because in the first line, we would lose the el at tmp.next . Which is required for the second line. So first do:
            # cur.next = tmp.next and then point the tmp to cur: tmp.next = cur
            cur.next = tmp.next
            tmp.next = cur

            # Note: If we don't update cur here, it remains behind of prev but at the right place. But since cur at the moment is always less than
            # `prev`, it would never execute the if block and we'll stuck at the inner while loop forever!
            cur = prev.next

        # here, returning `head` is wrong. Because the head might've been changed in the algo, because it was larger than some of the
        # els a head of it originally. But the dummy node is still pointing to the correct head. So we can use it to return the head.
        return dummy.next
