# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        p1 = 0
        p2 = 0
        n = len(players)
        m = len(trainers)
        cnt = 0

        while p1 < n and p2 < m:
            if players[p1] > trainers[p2]:
                p2 += 1
            else:
                cnt += 1
                p1 += 1
                p2 += 1

        return cnt