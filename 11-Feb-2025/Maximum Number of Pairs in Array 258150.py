# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        nums = Counter(nums)
        pairs = 0
        leftOvers = 0
        for n in nums.values():
            pairs += n // 2
            leftOvers += n % 2

        return [pairs, leftOvers]

        