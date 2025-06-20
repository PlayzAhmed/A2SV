# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        visited = set()
        prevLen = 0
        ans = 0

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0 or (i, j) in visited: return
            

            visited.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j]:
                    prevLen = len(visited)
                    dfs(i, j)
                    ans = max(ans, len(visited)-prevLen)

        return ans