# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution(object):
    def interpret(self, command):
        ans = ""
        i = 0

        while i < len(command):
            if command[i] == "G":
                ans += "G"
                i += 1
            elif i + 1 < len(command) and command[i+1] == ")":
                ans += "o"
                i += 2
            else:
                ans += "al"
                i += 4

        return ans

        