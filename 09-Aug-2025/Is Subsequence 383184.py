# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        
        i = 0
        j = 0

        while i < len(s):
            flag = False

            while j < len(t):
                if s[i] == t[j]:
                    flag = True
                j += 1
                if flag: break
            
            i += 1

            if not flag: return False

        return True