# 1. Brute Force
# T: O(n) for getMin() And O(1) for other ops
# M:  O(n) for getMin() And O(1) for other ops
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    # T: O(n)
    def getMin(self) -> int:
        # NOTE: We can't traverse a stack. Since a stack has only a push() at the end, pop() from the end and peak() methods.
        # So in order to kinda see all els, we need another stack(tmp) and we're gonna pop from our original stack and append to tmp.
        # At the same time, we do our logic(here, determining the min). Then we put els from tmp back to original stack.
        # Note that the order of els is maintained.
        tmp = []
        mini = self.stack[-1]

        while self.stack:
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while tmp:
            self.stack.append(tmp.pop())

        return mini


# 2. Two Stacks
# all of the methods are in O(1) time
# T: O(1) for all methods
# M: O(1) for all methods
class MinStack2:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # minStack could be empty, so consider that as well
        if self.minStack:
            val = min(val, self.minStack[-1])
        # Or instead of the above if, we could say: val = min(val, self.minStack[-1] if self.minStack else val)

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # per description, this func is only gonna get called when the stack is non-empty
    def top(self) -> int:
        return self.stack[-1]

    # per description, this func is only gonna get called when the stack is non-empty
    def getMin(self) -> int:
        return self.minStack[-1]


class MinStack3:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.stack:
            return

    def top(self) -> int:
        top = self.stack[-1]

        if top > 0:
            return top + self.min

        return self.min

    def getMin(self) -> int:
        return self.min
