# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        idxs = []
        adj = 0
        l = 0
        last = -1
        mx = 0

        for r in range(len(s)):
            if s[r] == last:
                adj += 1
                idxs.append(r)
            
            if adj > 1:
                adj -= 1
                l = idxs[-2]
            
            last =  s[r]
            mx = max(mx, r - l + 1)

        return mx