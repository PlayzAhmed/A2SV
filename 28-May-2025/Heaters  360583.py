# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        res = 0

        for house in houses:
            res = max(self.getClosestHeater(house, heaters), res)

        return res

    def getClosestHeater(self, house, heaters):
        left, right = 0, len(heaters) - 1
        radius = float('inf')

        while left <= right:
            mid = (left + right) // 2
            
            if heaters[mid] > house:
                right = mid - 1
            elif heaters[mid] < house:
                left = mid + 1
            else:
                return 0
            
            radius = min(abs(heaters[mid] - house), radius)

        return radius
        