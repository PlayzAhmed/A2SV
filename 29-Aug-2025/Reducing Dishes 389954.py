# Problem: Reducing Dishes - https://leetcode.com/problems/reducing-dishes/

class Solution(object):
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()
        cache = {}

        def dfs(i=0, coefficient=1):
            if i >= len(satisfaction):
                return 0
            if (i, coefficient) in cache:
                return cache[i, coefficient]

            cache[i, coefficient] = max(coefficient * satisfaction[i] + dfs(i+1, coefficient+1), dfs(i+1, 1))

            return cache[i, coefficient]

        return dfs()