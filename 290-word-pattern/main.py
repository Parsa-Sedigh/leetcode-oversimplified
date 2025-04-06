class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapPs, mapSp = {}, {}
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if ((pattern[i] in mapPs and mapPs[pattern[i]] != words[i]) or
                    (words[i] in mapSp and mapSp[words[i]] != pattern[i])):
                return False

            mapPs[pattern[i]] = words[i]
            mapSp[words[i]] = pattern[i]

        return True
