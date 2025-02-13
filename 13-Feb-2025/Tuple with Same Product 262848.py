# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution(object):
    def tupleSameProduct(self, nums):
        dic = defaultdict(int)
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                p = nums[i]*nums[j]
                res += dic[p] * 8
                dic[p] += 1
        
        return res