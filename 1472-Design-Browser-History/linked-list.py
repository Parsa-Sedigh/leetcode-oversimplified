class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        # We check if `self.cur.prev` is not None instead of `self.cur` . Why? Because this way, we will end up stopping as soon as
        # we reached the first node because the first node's prev is None, so we stop there.
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1

        return self.cur.val


    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1

        return self.cur.val