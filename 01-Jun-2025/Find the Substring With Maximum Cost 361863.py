# Problem: Find the Substring With Maximum Cost - https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution(object):
    def maximumCostSubstring(self, s, chars, vals):
        mp = {chr(i+97):i+1 for i in range(26)}

        for i in range(len(chars)):
            mp[chars[i]] = vals[i]

        ans = 0
        maxEnding = 0
        for ch in s:
            maxEnding = max(maxEnding + mp[ch], mp[ch])
            ans = max(ans, maxEnding)

        return ans
        