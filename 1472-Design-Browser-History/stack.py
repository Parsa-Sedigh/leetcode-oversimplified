# Array Implementation
class BrowserHistory:
    def __init__(self, homepage: str):
        # current page
        self.i = 0

        # The reason we have a separate variable for this and we can't just take the length of our self.history is
        # because this is the real length. We don't consider the length of self.history to be the real length.
        self.len = 1
        self.history = [homepage]

    # If we wanted to manually erase the forward history, like we popped every value after `self.i`, it would be O(n).
    # We don't need to do that, we don't need to delete those values, we cn sorta soft-delete them.
    # T: O(1)
    def visit(self, url: str) -> None:
        # We can only overwrite the next index after i, when there is actually an element in that position. How we can find out
        # if there's an element there? When length of history is more than self.i by 2. In other words: len(self.history) < self.i + 2
        # For example: If length of history is 3 and `i` is 2(last element), we can't overwrite the next element of `i`. The length
        # should be at least 4. Hence, the `+ 2` part.
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            # set the next history element to `url`
            self.history[self.i + 1] = url

        # we went to visit a new url, so update `i`
        self.i += 1

        # Instead of manually deleting the forward history, we just update `len` to reflect where `i` is currently at.
        # So even though the next elements are still there, we do not consider them, even though they still take up memory.
        self.len = self.i + 1

    # moving backwards, does not change the length of self.history. Because moving backwards does not delete anything.
    # T: O(1)
    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)

        return self.history[self.i]

    # Without using max()
    def back2(self, steps: int) -> str:
        index = 0
        if steps < self.i:
            index = self.i - steps

        self.i = index

        return self.history[index]

    # moving backwards, does not change the length of self.history.
    # T: O(1)
    def forward(self, steps: int) -> str:
        # We don't want self.i + steps to go out of bounds. Note that we don't use len(self.history) here.
        self.i = min(self.i + steps, self.len - 1)

        return self.history[self.i]