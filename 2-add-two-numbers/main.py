class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we're gonna create a result LL. So create a dummy node to avoid of edge cases of inserting into an empty LL.
        dummy = ListNode()
        cur = dummy
        carry = 0

        # what if we had sth like 8 + 7? We need to consider carry creating a new digit. So add the check of `or carry` in the condition of
        # while loop. In that case, v1 and v2 gonna be 0 but carry gonna be 1.
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # compute the new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next