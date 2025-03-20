# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution(object):
    def appendCharacters(self, s, t):
        p = 0
        n = len(t)
        for x in s:
            if n == p:
                return 0

            if x == t[p]:
                p += 1

        return n - p
        