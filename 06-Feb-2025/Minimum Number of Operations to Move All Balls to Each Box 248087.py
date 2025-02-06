# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        balls = []
        res = [0]*n

        for i in range(n):
            if boxes[i] == '1':
                balls.append(i)

        for i in range(n):
            for j in range(len(balls)):
                res[i] += abs(i-balls[j])

        return res