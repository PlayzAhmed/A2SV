# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution(object):
    def findCircleNum(self, isConnected):
        ans = 0
        visited = set()

        def dfs(idx=0):
            if idx >= len(isConnected) or idx in visited:
                return

            visited.add(idx)

            for i in range(len(isConnected)):
                if i != idx and isConnected[idx][i]:
                    dfs(i)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                ans += 1

        return ans