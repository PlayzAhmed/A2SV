# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution(object):
    def subarraySum(self, nums, k):
        n = len(nums)
        freq = defaultdict(int)
        freq[0] += 1
        s = 0
        res = 0

        for i in range(n):
            s += nums[i]
            res += freq[s-k]
            freq[s] += 1

            
        return res