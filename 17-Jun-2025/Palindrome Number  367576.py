# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        r = ""
        x = str(x)
        for i in reversed(x):
            r += i

        return x == r