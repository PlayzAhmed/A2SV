# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):

        res = []

        for i in range(len(nums)):
            count = 0

            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[i] > nums[j]:
                    count += 1

            res.append(count)
        
        return res