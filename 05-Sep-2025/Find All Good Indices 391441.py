# Problem: Find All Good Indices - https://leetcode.com/problems/find-all-good-indices/

class Solution(object):
    def goodIndices(self, nums, k):
        n = len(nums)
        ans = []
        pre = [1] * n
        suf = [1] * n

        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                pre[i] += pre[i-1]

        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                suf[i] += suf[i+1]

        for i in range(k, len(nums)-k):
            if pre[i-1] >= k and suf[i+1] >= k:
                ans.append(i)

        return ans