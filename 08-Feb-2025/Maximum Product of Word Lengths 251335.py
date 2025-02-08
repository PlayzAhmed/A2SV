# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        words_set = {}
        ans = 0
        n = len(words)

        for w in words:
            bitw = 0
            for ch in w:
                bitw |= (1<<ord(ch)-ord('a'))
            words_set[w] = bitw

        for i in range(n):
            for j in range(n):
                if not (words_set[words[i]] & words_set[words[j]]):
                    ans = max(ans, len(words[i])*len(words[j]))

        return ans
        