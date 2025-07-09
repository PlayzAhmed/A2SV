# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        q = deque()
        q.append([0, 0, 0]) # row index, column index, path's length
        visited = set()

        def is_not_valid(i, j):
            return i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or (i, j) in visited or grid[i][j] == 1

        while q:
            i, j, l = q.popleft()

            if is_not_valid(i, j): continue
            if i == len(grid) - 1 and j == len(grid[0]) - 1: return l+1
            visited.add((i, j))

            q.append([i + 1, j, l+1])
            q.append([i - 1, j, l+1])
            q.append([i, j + 1, l+1])
            q.append([i, j - 1, l+1])
            q.append([i + 1, j + 1, l+1])
            q.append([i - 1, j + 1, l+1])
            q.append([i + 1, j - 1, l+1])
            q.append([i - 1, j - 1, l+1])

        return -1