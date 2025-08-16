# Problem: Jump Game II - https://leetcode.com/problems/jump-game-ii/description/

class Solution(object):
    def jump(self, nums):
        memo = defaultdict(int)

        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                memo[i] = float("inf")
                continue

            if i not in memo:
                memo[i] = memo[i+1] + 1
            
            for j in range(i+2, i+nums[i]+1):
                memo[i] = min(memo[i], memo[j]+1)

        return memo[0]