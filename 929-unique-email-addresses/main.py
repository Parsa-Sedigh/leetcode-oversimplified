from typing import List


# 1. Built-In Functions
# T: O(n * m)
# M: O(n)
# Where n is the number of strings in the array, and m is the average length of these strings.
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            local, domain = e.split('@')

            # in `local`, if we encounter a `+`, we don't care about anything that comes after it. So we only care about the first
            # part of the split.
            local = local.split('+')[0]
            local = local.replace('.', '')

            unique.add((local, domain))

        return len(unique)


# 2. Iteration
# T: O(n * m) - we go through every el in the input and for each one, we're going through each char
# M: O(n) - because in worst case, every email could be unique
class Solution2:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        # for each email:
        for e in emails:
            i, local = 0, ''

            # first construct the local. Look at each char by moving i forward(ignore '.'), until hitting + or @.
            while e[i] not in ["+", "@"]:
                if e[i] != '.':
                    local += e[i]

                i += 1

            # when we get to here, we're either at the first + or the only @. In either case, we don't want to consider
            # any char as the `local`. So move i forward.
            # NOTE: If we've hit @ at the last while loop which means there was no `+` char, this while loop won't execute.
            while e[i] != "@":
                i += 1

            # When we get to here, it means i is at where @ lives, so the NEXT char after that is where our domain starts.
            domain = e[i + 1:]

            unique.add((local, domain))

        return len(unique)
