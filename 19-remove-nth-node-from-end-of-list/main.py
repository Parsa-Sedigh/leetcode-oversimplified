# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # first put a distance equal to n between left and right
        while n >0 and right:
            right = right.next
            n -= 1

        # we need to remove nth node from the END. So move left and right until we reach the end of the linked list
        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next

        return dummy.next