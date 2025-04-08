# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution(object):
    def numberOfSubstrings(self, s):
        n = len(s)
        freq = defaultdict(int)
        l = 0
        res = 0

        for r in range(n):
            freq[s[r]] += 1

            while freq["a"] >= 1 and freq["b"] >= 1 and freq["c"] >= 1:
                res += n - r
                freq[s[l]] -= 1
                l += 1

        
        return res
        