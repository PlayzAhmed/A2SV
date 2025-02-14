# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution(object):
    def areOccurrencesEqual(self, s):
        a = Counter(s)
        prv = a[s[0]]
        for n in a.values():
            if n != prv:
                return False

        return True
        