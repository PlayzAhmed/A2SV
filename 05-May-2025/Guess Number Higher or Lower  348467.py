# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            op = guess(mid)

            if op == -1:
                right = mid - 1
            elif op:
                left = mid + 1
            else:
                return mid

        