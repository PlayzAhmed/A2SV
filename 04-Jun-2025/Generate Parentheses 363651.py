# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution(object):
    def generateParenthesis(self, n):
        ans = []

        def bt(s="(", opens=1, closes=0):
            if opens == closes == n:
                ans.append(s)
                return
            if closes > n or opens > n or closes > opens:
                return

            bt(s + "(", opens+1, closes)
            bt(s + ")", opens, closes+1)

        bt()
        return ans