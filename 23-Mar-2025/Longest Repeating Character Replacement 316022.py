# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        mx = 0
        freq = defaultdict(int)
        maxFreq = 0
        l = 0

        for r in range(n):           
            freq[s[r]] += 1
            maxFreq = max(freq.values())

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                maxFreq = max(freq.values())
                l += 1

            mx = max(mx, r - l + 1)

        return mx