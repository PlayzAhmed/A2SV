# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution(object):
    def nextGreaterElements(self, nums):
        index = 0
        stack = []
        res = []
        n = len(nums)

        for i in range(n):
            index = i + 1
            stack.append(nums[index%n])

            while stack and stack[-1] <= nums[i]:
                stack.pop()
                index += 1
                stack.append(nums[index%n])
                if index % n == i:
                    stack.append(-1)
                    break

            res.append(stack[-1])

        
        return res