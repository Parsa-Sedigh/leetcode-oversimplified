from typing import List


# 1. Brute Force
# T: O(n^2)
# M: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i - 2])
                    b = int(tokens[i - 1])
                    res = 0

                    if tokens[i] == "+":
                        res = a + b
                    elif tokens[i] == "-":
                        res = a - b
                    elif tokens[i] == "*":
                        res = a * b
                    elif tokens[i] == "/":
                        res = int(a / b)

                    # M: O(n)
                    tokens = tokens[:i - 2] + [str(res)] + tokens[i + 1:]

                    break

        return int(tokens[0])


class DoublyLinkedListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# 2. Doubly linked list
# A doubly linked list allows access to previous nodes (prev), which is essential for
# fetching the two operands before an operator. It simulates a stack by processing operands and operators in order,
# adjusting pointers to "pop" operands and "push" results.

# T: O(n)
# M: O(n)
class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedListNode(tokens[0])
        curr = head
        answer = 0

        ######  Step 1: Building the Doubly Linked List ######
        # The head node is already constructed. So we start at the next token(index 1).
        for i in range(1, len(tokens)):
            # Construct a new LL node and set it's prev pointer to curr. And set the next pointer of curr to this new node.
            curr.next = DoublyLinkedListNode(tokens[i], curr)
            curr = curr.next

        ###### Step 2: Evaluating the Expression ######
        # since we have a doubly linked list at this point, we can use head for traversing the LL. We won't lose the linked list,
        # since there are `prev` pointers at each node and we can use them to go backwards
        while head is not None:
            if head.val in "+-*/":
                a = int(head.prev.prev.val)
                b = int(head.prev.val)
                res = 0

                if head.val == "+":
                    res = a + b
                elif head.val == "-":
                    res = a - b
                elif head.val == "*":
                    res = a * b
                elif head.val == "/":
                    res = int(a / b)

                # head currently contains an operator. But now we change it to contain the result of operation with `a` and `b`.
                # And then remove `a` and `b`, since they got calculated.
                head.val = str(res)
                head.prev = head.prev.prev.prev

                if head.prev is not None:
                    head.prev.next = head

            answer = int(head.val)
            head = head.next

        return answer


# 3. Recursion
# T: O(n)
# M: O(n)
class Solution3:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs() -> int:
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)

            # get the right operand
            right = dfs()
            left = dfs()

            if token == "+":
                return left + right
            elif token == "-":
                return left - right
            elif token == "*":
                return left * right
            elif token == "/":
                return int(left / right)

        return dfs()


# 4. Stack
# T: O(n)
# M: O(n)
class Solution4:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # The order of operands in - and / is important. The left operand is two previous operand and the right one is
                # previous one.
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()

                # to round towards zero, use int() which will convert it into integer and also round it towards zero at the same time
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]
