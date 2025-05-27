# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution(object):
    def smallestEvenMultiple(self, n):
        return n * 2 if n % 2 else n
        