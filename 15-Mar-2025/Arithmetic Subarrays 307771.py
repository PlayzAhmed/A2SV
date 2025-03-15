# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        res = []
        for i in range(len(l)):
            a = sorted(nums[l[i]:r[i]+1])
            diff = a[1] - a[0]
            valid = True
            for j in range(1, len(a)-1):
                if a[j+1] - a[j] != diff:
                    valid = False
                    break
            res.append(valid)
        
        return res

        