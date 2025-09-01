# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        n = len(nums)
        nums = list(map(str, nums))
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return str(int("".join(map(str, nums))))
                    