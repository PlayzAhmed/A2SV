# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        pre = [nums[0]] * n
        suf = [nums[n-1]]
        res = []

        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i]

        for i in range(n-2, -1, -1):
            suf.insert(0, suf[0] * nums[i])
        
        for i in range(n):
            if i == 0:
                res.append(suf[1])
            elif i == n-1:
                res.append(pre[i-1])
            else:
                res.append(pre[i-1]*suf[i+1])

        return res