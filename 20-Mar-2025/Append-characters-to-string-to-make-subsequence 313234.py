# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

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
        