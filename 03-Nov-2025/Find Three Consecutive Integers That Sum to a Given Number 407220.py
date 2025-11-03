# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution(object):
    def sumOfThree(self, num):
        nums = [num//3 - 1, num//3, num//3 + 1]

        if sum(nums) == num:
            return nums
        return []
        