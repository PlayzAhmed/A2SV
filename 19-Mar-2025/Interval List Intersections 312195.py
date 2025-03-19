# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution(object):
    def intervalIntersection(self, f, s):
        p1 = 0
        p2 = 0
        n = len(f)
        m = len(s)
        res = []

        while p1 < n and p2 < m:
            x = max(f[p1][0], s[p2][0])
            y = min(f[p1][1], s[p2][1])

            if x <= y:
                res.append([x, y])
                if y == f[p1][1]:
                    p1 += 1
                else:
                    p2 += 1
            else:
                if f[p1][0] < s[p2][1]:
                    p1 += 1
                else:
                    p2 += 1
        
        return res