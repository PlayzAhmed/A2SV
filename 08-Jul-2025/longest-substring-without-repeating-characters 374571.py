# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq = defaultdict(int)
        l = 0 
        mx = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1

            mx = max(mx, r - l + 1)

        return mx
            