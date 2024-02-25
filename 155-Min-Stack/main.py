# all of the methods are in O(1) time
class MinStack:

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


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()