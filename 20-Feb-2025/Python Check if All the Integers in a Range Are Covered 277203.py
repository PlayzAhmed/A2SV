# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution(object):
    def isCovered(self, ranges, left, right):
        arr = []
        r = range(left, right+1)

        for s, e in ranges:
            for n in range(s, e+1):
                arr.append(n)

        for i in r:
            if i not in arr:
                return False

        return True

        