# Problem: Maximum Score After Splitting a String - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution(object):
    def maxScore(self, s):
        suf = [0] * (len(s) + 1)

        for i in range(len(s)-1, -1, -1):
            suf[i] += suf[i+1] + int(s[i])

        ans = 0
        count = 0

        for i in range(len(s)-1):
            if s[i] == "0":
                count += 1
            
            ans = max(ans, count + suf[i+1])
        
        return ans