# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        s = list(s)
        t = list(t)
        i = 0

        while i < len(s):
            if i == 0 and s[i] == "#":
                s.pop(i)
            elif s[i] == "#":
                s.pop(i)
                s.pop(i-1)
                i -= 1
            else:
                i+= 1

        i = 0

        while i < len(t):
            if i == 0 and t[i] == "#":
                t.pop(i)
            elif t[i] == "#":
                t.pop(i)
                t.pop(i-1)
                i -= 1
            else:
                i += 1

        print(s, t)

        return s == t

        