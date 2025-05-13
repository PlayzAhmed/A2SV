# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution(object):
    def shipWithinDays(self, weights, days):
        left, right, = min(weights), sum(weights)
        ans = -1
        while left <= right:
            mid = (left+right) // 2

            if self.checkCapacity(weights, days, mid):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans

    def checkCapacity(self, weights, days, cap):
        s = 0
        d = 1
        for weight in weights:
            if s + weight <= cap:
                s += weight
            elif weight <= cap:
                d += 1
                s = weight
            else:
                return False

        return d <= days
        