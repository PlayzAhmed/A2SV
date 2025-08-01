# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution(object):
    def minMoves(self, target, maxDoubles):
        moves = 0
        while target > 1 and maxDoubles:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1

            moves += 1
            
        return moves + target - 1