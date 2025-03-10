# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        lower = 0
        higher = len(height)-1
        res = 0
        
        while lower < higher:
            res = max(res, min(height[lower], height[higher])*abs(lower-higher))

            if height[lower] > height[higher]:
                higher -= 1
            else:
                lower += 1

        return res