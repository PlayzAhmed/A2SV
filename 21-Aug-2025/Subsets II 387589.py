# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution(object):
    def subsetsWithDup(self, nums):
        ans = []
        n = len(nums)

        for i in range(1 << n):
            temp = []

            for j in range(n):
                if i & (1 << j):
                    temp.append(nums[j])
            
            temp.sort()
            if temp not in ans:
                ans.append(temp)

        return ans
        