# Problem: Maximum Number of Operations With the Same Score II - https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/description/

class Solution(object):
    def maxOperations(self, nums):
        n = len(nums)
        cache = defaultdict(int)

        def dfs(l, r, score):
            if l >= r:
                return 0

            if (l, r, score) in cache:
                return cache[(l, r, score)]

            if nums[l] + nums[l+1] == score:
                cache[(l, r, score)] = max(cache[(l, r, score)], 1 + dfs(l+2, r, score))

            if nums[r] + nums[r-1] == score:
                cache[(l, r, score)] = max(cache[(l, r, score)], 1 + dfs(l, r-2, score))

            if nums[l] + nums[r] == score:
                cache[(l, r, score)] = max(cache[(l, r, score)], 1 + dfs(l+1, r-1, score))

            return cache[(l, r, score)]

        return 1 + max(dfs(2, n-1, nums[0]+nums[1]), dfs(0, n-3, nums[-1]+nums[-2]), dfs(1, n-2, nums[0]+nums[-1]))