# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution(object):
    def balancedStringSplit(self, s):
        r = 0
        c = 0

        for ch in s:
            if ch == 'R':
                r += 1
            else:
                r -= 1

            if r == 0:
                c += 1

        return c
        