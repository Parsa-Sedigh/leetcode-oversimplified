from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for i in range(len(accounts)):
            for email in accounts[1:]:
