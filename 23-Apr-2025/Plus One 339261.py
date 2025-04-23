# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        return [int(y) for y in str(int("".join([str(x) for x in digits])) + 1)]