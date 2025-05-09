# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution(object):
    def find132pattern(self, nums):
        stack = []
        curMin = nums[0]
        
        for i in range(1, len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()

            if stack and stack[-1][1] < nums[i]:
                return True

            stack.append((nums[i], curMin))
            curMin = min(curMin, nums[i])
        return False