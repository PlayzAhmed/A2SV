# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution(object):
    def gameOfLife(self, board):
        rows = len(board)
        cols = len(board[0])

        res = copy.deepcopy(board)

        for row in range(rows):
            for col in range(cols):
                lives = 0
                deads = 0
                if row+1 < rows:
                    if res[row+1][col] == 1:
                        lives += 1
                    else:
                        deads += 1
                    
                    if col+1 < cols:
                        if res[row+1][col+1] == 1:
                            lives += 1
                        else:
                            deads += 1

                    if col-1 >= 0:
                        if res[row+1][col-1] == 1:
                            lives += 1
                        else:
                            deads += 1
                
                if row-1 >= 0:
                    if res[row-1][col] == 1:
                        lives += 1
                    else:
                        deads += 1

                    if col+1 < cols:
                        if res[row-1][col+1] == 1:
                            lives += 1
                        else:
                            deads += 1

                    if col-1 >= 0:
                        if res[row-1][col-1] == 1:
                            lives += 1
                        else:
                            deads += 1

                if col+1 < cols:
                    if res[row][col+1] == 1:
                        lives += 1
                    else:
                        deads += 1

                if col-1 >= 0:
                    if res[row][col-1] == 1:
                        lives += 1
                    else:
                        deads += 1

                if (res[row][col] == 1 and (lives == 2 or lives == 3)) or (res[row][col] == 0 and lives == 3):
                    board[row][col] = 1
                else:
                    board[row][col] = 0