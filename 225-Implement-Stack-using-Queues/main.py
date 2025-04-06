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


# 2. Using Two Queues
class MyStack2:

    # T: O(1)
    # M: O(1)
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # q1: Our current stack
    # q2: At each call to push(), it's empty. Then it gets the new val, then we move all q1 els(which form a stack) to the end of q2.
    # Making the new val at the front of the whole sequence. Then we move els back to q1 where we hold the current stack.

    # The push method ensures LIFO behavior by:
    #
    # 1. Using q2 as a temporary holding area for the new element x.
    # 2. Moving all existing elements from q1 to q2, placing them behind x.
    # 3. Swapping the queues so q1 becomes the main stack with x at the front.

    # At each call, q2 is empty, since we moved all q1 els to q2 and then q1 became empty, then we assigned q1 to q2.
    # Since q2 is empty, after calling push(), it ony has the pushed val.
    # Then we move all front els of q1 to the back of q2.

    # T: O(n)
    # M: O(n)
    def push(self, x: int) -> None:
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    # T: O(1)
    # M: O(1)
    def pop(self) -> int:
        return self.q1.popleft()

    # T: O(1)
    # M: O(1)
    def top(self) -> int:
        return self.q1[0]

    # T: O(1)
    # M: O(1)
    def empty(self) -> bool:
        return len(self.q1) == 0


# 2. Using One Queue
# M: O(n)
class MyStack3:

    # T: O(1)
    def __init__(self):
        # deque() creates a double ended queue. But we won't use any of those advanced features. We'll just stick to using it as if
        # it were just a regular queue.
        self.q = deque()

    # T: O(1)
    def push(self, x: int) -> None:
        # appends to the right side of the queue(end)
        self.q.append(x)

    # T: O(n)
    def pop(self) -> int:
        for i in range(0, len(self.q) - 1):
            self.push(self.q.popleft())

            # or:
            # self.q.append(self.q.popleft())

        # pop the last value(do not push it, since we wanna remove the last one)
        return self.q.popleft()

    # T: O(1)
    def top(self) -> int:
        return self.q[-1]  # or return self.q[len(self.q) - 1]

    # T: O(1)
    def empty(self) -> bool:
        return len(self.q) == 0


# 3. Queue Of Queues
# M: O(n)
class MyStack4:

    # T: O(1)
    def __init__(self):
        self.q = None

    # T: O(1)
    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    # T: O(1)
    def pop(self) -> int:
        top = self.q.popleft()
        self.q = self.q.popleft()

        return top

    # T: O(1)
    def top(self) -> int:
        return self.q[0]

    # T: O(1)
    def empty(self) -> bool:
        return self.q is None

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
