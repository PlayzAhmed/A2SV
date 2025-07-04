# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution(object):
    def updateMatrix(self, mat):
        q = deque()
        visited = set()
        ROWS = len(mat)
        COLS = len(mat[0])

        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0: q.append([i, j, 0])
                else: mat[i][j] = -1

        def not_valid_point(i, j):
            return i >= ROWS or j >= COLS or i < 0 or j < 0 or (i, j) in visited

        while q:
            i, j, l = q.popleft()

            if not_valid_point(i, j): continue

            visited.add((i, j))

            if mat[i][j] == -1: mat[i][j] = l

            q.append([i + 1, j, l + 1])
            q.append([i - 1, j, l + 1])
            q.append([i, j + 1, l + 1])
            q.append([i, j - 1, l + 1])


        return mat