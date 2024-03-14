from collections import deque


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# My approach - doubly linked list
class MyStack:

    def __init__(self):
        self.left = self.right = None

    def push(self, x: int) -> None:
        if self.right:
            node = ListNode(x)
            node.prev = self.right
            self.right.next = node
            self.right = self.right.next
        else:
            self.left = self.right = ListNode(x)

    def pop(self) -> int:
        if not self.right:
            return -1


        val = self.right.val
        self.right = self.right.prev
        if self.right:
            self.right.next = None

        return val

    def top(self) -> int:
        return self.right.val

    def empty(self) -> bool:
        return self.right == None

class MyStack2:

    def __init__(self):
        # deque() creates a double ended queue. But we won't use any of those advanced features. We'll just stick to using it as if
        # it were just a regular queue.
        self.q = deque()

    def push(self, x: int) -> None:
        # appends to the right side of the queue(end)
        self.q.append(x)

    # O(n)
    def pop(self) -> int:
        for i in range(0, len(self.q) - 1):
            self.push(self.q.popleft())

            # or:
            # self.q.append(self.q.popleft())

        # pop the last value(do not push it, since we wanna remove the last one)
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1] # or return self.q[len(self.q) - 1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()