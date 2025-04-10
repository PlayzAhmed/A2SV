# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        res = ""
        for i in range(n):
            for j in range(i, n):
                w = s[i:j+1]
                if w == w[::-1]:
                    if len(w) > len(res):
                        res = w

        return res
