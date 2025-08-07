# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        ROWS = len(dungeon)
        COLS = len(dungeon[0])

        dp = [[1] * COLS for _ in range(ROWS)]
        dp[ROWS-1][COLS-1] = min(dungeon[ROWS-1][COLS-1], 0)

        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                if (i, j) != (ROWS-1, COLS-1):
                    cur = dungeon[i][j]
                    right = float('-inf') if j + 1 >= COLS else dp[i][j+1] + cur
                    down = float('-inf') if i + 1 >= ROWS else dp[i+1][j] + cur

                    dp[i][j] = min(max(right, down), 0)

        return 1-dp[0][0]