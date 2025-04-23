# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        s_stack = []
        t_stack = []

        for x in s:
            if x == "#" and s_stack:
                s_stack.pop()
            elif x != "#":
                s_stack.append(x)

        for x in t:
            if x == "#" and t_stack:
                t_stack.pop()
            elif x != "#":
                t_stack.append(x)

        
        return s_stack == t_stack
        