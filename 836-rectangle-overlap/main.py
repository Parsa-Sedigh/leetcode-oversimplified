from typing import List


# two conditions need to be valid at the same time:
# 1. top-right of rec1 should always be grater than bottom-left of rec2
# 2. top-right of rec2 should be greater than bottom-left or rec1
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (rec1[2] > rec2[0] and rec1[3] > rec2[1]) and (rec2[2] > rec1[0] and rec2[3] > rec1[1])
