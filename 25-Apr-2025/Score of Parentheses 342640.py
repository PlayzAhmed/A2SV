# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                temp = 0
                while stack and stack[-1] != "(":
                    temp += stack.pop()
                stack.pop()
                stack.append(2*temp if temp else 1)
            else:
                stack.append(s[i])

        return sum(stack)
        