# Problem: Get Maximum in Generated Array - https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution(object):
    def getMaximumGenerated(self, n):
        if n < 2:
            return n
            
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        mx = 1
        
        for i in range(2, n+1):
            if i % 2:
                nums[i] = nums[i//2] + nums[i//2 + 1]
            else:
                nums[i] = nums[i//2]

            mx = max(mx, nums[i])

        return mx