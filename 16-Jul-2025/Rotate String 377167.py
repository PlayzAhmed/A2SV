# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution(object):
    def rotateString(self, s, goal):
        res = []

        for i in range(len(s)):
            res.append(s)
            s = s[1:] + s[0]
                    
        res.append(s)

        if goal in res: return True
        return False
        