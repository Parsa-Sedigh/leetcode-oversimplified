# M: O(n)
class MyQueue:
    def __init__(self):
        # s stands for stack
        self.s1 = []
        self.s2 = []

    # T: O(n)
    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())

        self.s2.append(x)

        while self.s2:
            self.s1.append(self.s2.pop())

    # T: O(1)
    def pop(self) -> int:
        return self.s1.pop()

    # T: O(1)
    def peek(self) -> int:
        return self.s1[-1]

    # T: O(1)
    def empty(self) -> bool:
        return len(self.s1) == 0


# 2. Using Two Stacks (Amortized Complexity)
# M: O(n)
class MyQueue2:
    # T: O(1)
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # T: O(1)
    def push(self, x: int) -> None:
        self.s1.append(x)

    # T: O(1)
    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    # T: O(1)
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    # T: O(1)
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
        # OR:
        # return max(len(self.s1), len(self.s2)) == 0
