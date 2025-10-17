# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution(object):
    def carFleet(self, target, position, speed):
        speed = sorted((position[i], float(target - position[i]) / speed[i]) for i in range(len(speed)))
        last = speed[-1][1]
        ans = 1

        while speed:
            _, s = speed.pop()
            if s > last:
                ans += 1
                last = s

        return ans