# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution(object):
    def findTheWinner(self, n, k):
        players = range(1, n+1)
        i = 0

        while len(players) > 1:
            i = (i+k-1) % len(players)

            players.pop(i)

        return players[0]
        