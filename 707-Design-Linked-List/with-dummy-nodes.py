# TODO: Implement singly with dummy nodes

class DoublyListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyDoublyLinkedList:
    def __init__(self):
        # dummy nodes
        self.head = DoublyListNode(0)
        self.tail = DoublyListNode(0)

        # connect the initial nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0

        while cur and i == index:
            cur = cur.next
            i += 1

        return cur.val

    # or by decrementing given index:
    # def get(self, index: int) -> int:
    #     cur = self.head.next
    #
    #     while cur and index > 0:
    #         cur = cur.next
    #         index -= 1
    #
    #     # Note: We can't just return the result here. Because we have to make sure that we haven't gone out of bounds. So make sure `curr`
    #     # is not None.
    #     # Note: And we have to make sure we haven't reached the end of the linked list because we have a dummy node, what happens if
    #     # our curr is at the dummy node. We definitely don't want to return that node as the result(that's considered out of bounds).
    #     # So check for cur != self.tail
    #     # Note: index has to be equal to 0 because otherwise that means the while loop exited before we were able to reach the `index`.
    #     # That would happen if our linked list was too small. So check for: index == 0
    #
    #     if cur and cur != self.tail and index == 0:
    #         return cur.val
    #
    #     return -1

    def addAtHead(self, val: int) -> None:
        node = DoublyListNode(val)
        next = self.head.next
        prev = self.head

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node = DoublyListNode(val)
        next = self.tail
        prev = self.tail.prev

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev

    # Note: We're inserting BEFORE the given index. So if we arrive at the self.tail, we're gonna insert the node in a way that
    # it's next, point to self.tail . But if we go out of bounds(meaning we passed the self.tail dummy node), then we can't insert the node.
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        # We need to check if we're in a valid position
        if cur and index == 0:
            node = DoublyListNode(val)
            next = cur
            prev = cur.prev

            prev.next = node
            next.prev = node

            node.next = next
            node.prev = prev

    # We delete the node itself that the cur lands at(arrives at). So if the cur lands at dummy nodes, we won't delete the dummy node because
    # it's not a valid node. So in that case, we won't perform the delete op. Similarly, we won't do delete, if we go out of bounds(when we
    # pass the dummy node)
    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.tail and index == 0:
            next = cur.next
            prev = cur.prev

            prev.next = cur.next
            next.prev = cur.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)