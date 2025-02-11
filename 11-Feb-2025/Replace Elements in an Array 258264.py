# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution(object):
    def arrayChange(self, nums, operations):
        numsMap = {nums[i]:i for i in range(len(nums))}
        
        for num, newNum in operations:
            nums[numsMap[num]] = newNum
            numsMap[newNum] = numsMap[num]
            numsMap.pop(num)

        return nums