# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution(object):
    def minWindow(self, s, t):
        if t == "": return ""
        freq, t = defaultdict(int), Counter(t)
        have, need = 0, len(t)
        l = 0
        res, resLen = "", float('inf')

        for r in range(len(s)):
            freq[s[r]] += 1

            if t[s[r]] > 0 and freq[s[r]] == t[s[r]]:
                have += 1

            while have == need:
                if resLen > (r - l + 1):
                    resLen = r - l + 1
                    res = s[l:r+1]
                
                freq[s[l]] -= 1
                if t[s[l]] > 0 and freq[s[l]] < t[s[l]]:
                    have -= 1
                l += 1

        return res