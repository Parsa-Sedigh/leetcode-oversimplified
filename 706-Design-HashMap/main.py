class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

# my solution
class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(0, 0) for i in range(10**4)]

    def hash(self, key: int):
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        cur = self.hashmap[index]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value

                return

            cur = cur.next

        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.hashmap[index]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val

            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.hashmap[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next

                return

            cur = cur.next

#############################################

# Approach 2: Using Separate Chaining(linked list) to workaround collisions.
class MyHashMap2:
    def __init__(self):
        # 1000 is given in the description
        self.map = [ListNode() for i in range(10000)]

    def hash(self, key: int):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        cur = self.map[index]

        # if we said: `while cur`, at the end of the loop, the cur would be None, but that's not where we want to end. We want
        # cur to be pointing at the last node(so it's next field will be None), so we say: while `while cur.next`.
        while cur.next:
            # Note: Also remember the cur will start at the dummy node, so we use cur.next.<whatever>,
            # not just cur.<whatever>. If you don't do this, yes the cur would still point at the last element of the
            # linked list after the loop is done, but it won't check the body of the loop for the last node. We want
            # to check the body of the loop for the last node as well to see if it can be overwritten. Another reason is we don't want to check
            # the if block for the dummy node as well, so use cur.next.<whatever> .
            if cur.next.key == key:
                cur.next.val = value

                return

            cur = cur.next

        # we reached the end of the linked list
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.map[index] # you can pass .next, like: cur = self.map[index].next, because we don't want to start at the dummy node

        while cur:
            if cur.key == key:
                return cur.val

            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)

        # We can't start at the next node of dummy node, because we're gonna need to do pointer manipulation
        cur = self.map[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next

                return

            cur = cur.next

#############################################