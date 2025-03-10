# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution(object):
    def mergeAlternately(self, word1, word2):
        n = len(word1)
        m = len(word2)
        l = max(n, m)
        res = ""

        for i in range(l):
            if i < n:
                res += word1[i]
            
            if i < m:
                res += word2[i]

        return res
        