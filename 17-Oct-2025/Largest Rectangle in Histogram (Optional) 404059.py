# Problem: Largest Rectangle in Histogram (Optional) - https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        ans = 0

        for i in range(n):
            if not stack:
                stack.append((heights[i], i))
                continue

            index = i

            while stack and heights[i] < stack[-1][0]:
                h, index = stack.pop()

                ans = max(ans, h*(i-index))
                
            stack.append((heights[i], index))

        while stack:
            h, i = stack.pop()
            ans = max(ans, h * (n-i))

        return ans