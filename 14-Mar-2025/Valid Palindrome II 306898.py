# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution(object):
    def removeChar(self, s):
        n = len(s)
        i = 0
        j = n - 1

        while i <= j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1

        return True


    def validPalindrome(self, s):
        n = len(s)
        i = 0
        j = n-1
        while i <= j:
            if s[i] == s[j]:
                j -= 1
                i += 1
            else:
                return self.removeChar(s[i:j]) or self.removeChar(s[i+1:j+1])

        return True