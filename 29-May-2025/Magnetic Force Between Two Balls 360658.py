# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution(object):
    def maxDistance(self, position, m):
        left, right = 0, max(position)
        position.sort()
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if self.magneticForce(mid, position, m):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def magneticForce(self, distance, position, m):
        count = 1
        last = position[0]

        for i in range(1, len(position)):
            if position[i] - last >= distance:
                count += 1
                last = position[i]
                if count == m:
                    return True
        
        return False

        