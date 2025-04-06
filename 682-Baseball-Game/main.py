from typing import List


# 1. Stack
# T: O(n)
# M: O(n)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


# 2. Stack - II
# T: O(n)
# M: O(n)
class Solution2:
    def calPoints(self, operations: List[str]) -> int:
        # we need stack to remember the vals
        stack, res = [], 0

        for op in operations:
            if op == "+":
                op_res = stack[-1] + stack[-2]

                res += op_res
                stack.append(op_res)
            elif op == "D":
                op_res = 2 * stack[-1]

                res += op_res
                stack.append(op_res)
            elif op == "C":
                res -= stack.pop()
            else:
                res += int(op)
                stack.append(int(op))

        return res
