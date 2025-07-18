# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution(object):
    def findMinArrowShots(self, points):
        ans = []
        points.sort()

        def intersection():
            a, b = ans[-1]
            if a <= l and b >= r:
                ans[-1] = (l, r)
                return True
            elif a <= r and a >= l and b >= r:
                ans[-1] = (a, r)
                return True
            elif a <= l and b >= l and b <= r:
                ans[-1] = (l, b)
                return True
            elif a >= l and b <= r:
                return True
            return False
        
        for l, r in points:
            if not ans or not intersection():
                ans.append((l, r))

        return len(ans)