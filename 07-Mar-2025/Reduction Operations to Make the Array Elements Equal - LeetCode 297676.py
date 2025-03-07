# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution(object):
    def reductionOperations(self, nums):
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        op = 0

        for i in range(len(nums)-1, 0, -1):
            op += i * freq[nums[i]]

        return op