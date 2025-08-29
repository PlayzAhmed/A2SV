# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution(object):
    def minSteps(self, n):
        cache = {}

        def dfs(i=1, copy=1):
            if i == n:
                return 0
            if i > n:
                return 1000
            if (i, copy) in cache:
                return cache[i, copy]

            cache[(i, copy)] = min(1 + dfs(i+copy, copy), 2 + dfs(i+i, i))
            return cache[(i, copy)]

        if n == 1: return 0
        return 1 + dfs()