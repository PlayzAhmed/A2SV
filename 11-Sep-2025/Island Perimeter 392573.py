# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    def islandPerimeter(self, grid):
        size = [len(grid), len(grid[0])]
        ans = 0
        visited = set()

        def dfs(i, j):
            if (i, j) in visited: return 0
            if i >= size[0] or j >= size[1] or i < 0 or j < 0 or grid[i][j] == 0: return 1

            visited.add((i, j))
            
            return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)

        for i in range(size[0]):
            for j in range(size[1]):
                if grid[i][j] and (i, j) not in visited:
                    ans += dfs(i, j)

        
        return ans
        