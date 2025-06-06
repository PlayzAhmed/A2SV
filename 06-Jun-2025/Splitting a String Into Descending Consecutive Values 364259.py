# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution(object):
    def splitString(self, s):
        def backtrack(idx, prev):
            if idx == len(s):
                return True
            
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                if val + 1 == prev and backtrack(i+1, val):
                    return True
            return False

        for i in range(len(s)-1):
            if backtrack(i+1, int(s[:i+1])): return True

        return False