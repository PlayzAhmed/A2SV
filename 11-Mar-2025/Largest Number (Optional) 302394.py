# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        n = len(nums)
        nums = list(map(str, nums))
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return "".join(nums) if nums[0] != "0" else "0"                    