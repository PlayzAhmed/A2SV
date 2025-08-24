# Problem: Last Stone Weight II - https://leetcode.com/problems/last-stone-weight-ii/description/

class Solution(object):
    def lastStoneWeightII(self, stones):
        stones_sum = sum(stones)
        target = ceil(stones_sum / 2)
        cache = {}

        def dfs(i=0, total=0):
            if total >= target or i >= len(stones):
                return abs(total - (stones_sum - total))

            if (i, total) in cache:
                return cache[i, total]

            cache[i, total] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))

            return cache[i, total]

        return dfs()
        