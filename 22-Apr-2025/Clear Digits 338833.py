# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution(object):
    def clearDigits(self, s):
        stack = []

        for x in s:
            if x.isdigit() and stack:
                stack.pop()
            elif not x.isdigit():
                stack.append(x)

        return "".join(stack)