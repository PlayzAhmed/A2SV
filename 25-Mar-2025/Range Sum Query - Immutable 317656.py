# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    def __init__(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        self.nums = nums
        

    def sumRange(self, left, right):
        return self.nums[right] if left == 0 else self.nums[right] - self.nums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)