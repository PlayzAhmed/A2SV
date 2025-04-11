# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution(object):
    def findAnagrams(self, s, p):
        n = len(p)
        p = Counter(p)
        res = []
        freq = Counter(s[:n])
        if freq == p:
            res.append(0)
        for r in range(n, len(s)):
            freq[s[r]] += 1
            freq[s[r-n]] -= 1

            if freq[s[r-n]] == 0:
                freq.pop(s[r-n])

            if freq == p:
                res.append(r-n+1)

        return res
     