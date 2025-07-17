# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution(object):
    def largestOddNumber(self, num):
        l = -1

        for r in range(len(num)):
            if int(num[r])% 2: l = r

        return num[:l+1]