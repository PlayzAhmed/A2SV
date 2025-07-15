# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)

        for i in range(len(nums)-2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if a + b > c and b + c > a and a + c > b: return a + b + c

        return 0
        