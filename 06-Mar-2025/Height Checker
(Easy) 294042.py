# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution(object):
    def heightChecker(self, heights):
        expected = copy.copy(heights)
        n = len(heights)
        cnt = 0

        for i in range(n):
            idx = i
            for j in range(i+1, n):
                if expected[idx] > expected[j]:
                    idx = j
            expected[idx], expected[i] = expected[i], expected[idx]

        if heights == expected:
            return 0 

        for i in range(n):
            if heights[i] != expected[i]:
                cnt += 1
                
        return cnt