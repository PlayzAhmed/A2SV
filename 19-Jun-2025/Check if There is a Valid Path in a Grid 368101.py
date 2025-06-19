# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution(object):
    def hasValidPath(self, grid):
        visited = set()

        def path(pos, direction):
            i, j = pos
            if direction == 1:
                return (i, j-1), (i, j+1)
            elif direction == 2:
                return (i-1, j), (i+1, j)
            elif direction == 3:
                return (i, j-1), (i+1, j)
            elif direction == 4:
                return (i, j+1), (i+1, j)
            elif direction == 5:
                return (i, j-1), (i-1, j)
            elif direction == 6:
                return (i, j+1), (i-1, j)

        def dfs(cur=(0, 0), prev=(0, 0)):
            i, j = cur

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited:
                return False
            
            first, sec = path(cur, grid[i][j])

            if first != prev and sec != prev and cur != (0, 0):
                return False

            visited.add((i, j))
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return True

            
            return dfs(first, cur) or dfs(sec, cur)

        return dfs()