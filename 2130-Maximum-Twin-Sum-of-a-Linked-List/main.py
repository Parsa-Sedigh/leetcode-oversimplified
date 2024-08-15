# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# T: O(n)
# M: O(1)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        # By the time this loop completes, since the LL is always gonna be of even list per description, the `fast` pointer
        # will be out of bounds and the `slow` will be at the beginning of the second half of the LL and `prev` will be one node
        # behind `slow`. So prev will be at the beginning of the left half(we have reversed the left half after this loop).
        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        res = 0

        # we could use the `prev` as the condition, because both halfs have even length.
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return res