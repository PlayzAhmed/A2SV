# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        n = len(s)
        ones = s.count("1")
        res = ""
        
        if ones > 1:
            res += "1"*(ones-1)
        res += "0"*(n-ones)
        res += "1"

        return res
        