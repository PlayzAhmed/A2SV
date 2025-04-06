# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution(object):
    def judgeSquareSum(self, c):
        start = 0
        end = ceil(sqrt(c))

        while start <= end:
            if pow(start, 2) + pow(end, 2) > c:
                end -= 1
            elif pow(start, 2) + pow(end, 2) < c:
                start += 1
            else:
                return True

        return False