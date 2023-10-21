import collections
from typing import List


class DetectSquares:

    def __init__(self):
        # We use defaultdict so if we try to retreive a key that hasn't already been inserted, then the default value of that will be zero.
        self.ptsCount = collections.defaultdict(int)

        # we can solve the question without this list
        self.pts = []

    def add(self, point: List[int]) -> None:
        # Note: In python, a list can't be a key in a hashmap. So we have to transform the point list into a tuple.
        # By using a defaultdict(int), if it doesn't already exist in the map, it's default value will be zero and then we'll add one to it.
        # So using a defaultdict will make code shorter.
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        # iterate over every single point in the list of points
        for x, y in self.pts:
            # Verify current point of the loop is actually a diagonal point for the query point. If current loop point is not a digonal point
            # just pass(continue).
            # Note: In the description, they say that the squares have to have a positive area, that means we can't just stack four points
            # at the exact same coordinate and call that a square(I don't know technicakky that is a square or not!) which would have zero area.
            # So we need to avoid that case, so x can't be equal to query point's x and the same for y.
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue

            # At this point, we know the loop variable and the query point are diagonal to each other, so now we wanna know can we
            # create a square with them or not? How can we know if we can create a square with them? Well the two other points should exist which are
            # (x, py) and (px, y) and we're gonna multiply the count of those two nodes together and it will give us how many squares we can create
            # with these four coordinates.
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)