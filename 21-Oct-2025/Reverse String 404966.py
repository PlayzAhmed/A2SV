# Problem: Reverse String - https://leetcode.com/problems/reverse-string/description/

class Solution(object):
    def reverseString(self, s):
        ns = len(s)
        n = ns // 2

        for i in range(n):
            s[i], s[ns - i - 1] = s[ns - i - 1], s[i]

        return s
        