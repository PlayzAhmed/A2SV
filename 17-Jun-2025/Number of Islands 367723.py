# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        visited = set()
        ans = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0" or (i, j) in visited:
                return

            visited.add((i, j))
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    ans += 1

        return ans