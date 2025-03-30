# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        mp = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        temp = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] =="[":
                temp.append(s[i])
            else:
                if temp and temp[-1] == mp[s[i]]:
                    temp.pop()
                else:
                    return False

        return False if temp else True