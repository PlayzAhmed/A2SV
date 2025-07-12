# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        s = Counter(s)
        t = Counter(t)

        for key, val in t.items():
            if val != s[key]: return key
        