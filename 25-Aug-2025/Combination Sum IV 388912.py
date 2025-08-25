# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution(object):
    def combinationSum4(self, nums, target):
        cache = defaultdict(int)
        cache[0] = 1

        for total in range(1, target+1):
            for num in nums:
                cache[total] += cache[total-num]

        return cache[target]