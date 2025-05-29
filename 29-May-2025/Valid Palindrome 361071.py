# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isPalindrome(self, s):
        new = ""

        for i in range(len(s)):
            if 'a' <= lower(s[i]) <= 'z' or s[i].isdigit():
                new += lower(s[i])

        return new == new[::-1]
        