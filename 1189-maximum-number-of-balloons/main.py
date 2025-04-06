# T: O()
# M: O()
from cassandra.cluster import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        target_i = 0
        words_num = 0

        text = list(text)

        for i in range(len(text)):
            found = False

            for j in range(len(text)):
                if text[j] == target[target_i]:
                    found = True
                    text[j] = None
                    target_i += 1

                    if target_i == len(target):
                        target_i = 0
                        words_num += 1

                    break

            if not found:
                break

        return words_num