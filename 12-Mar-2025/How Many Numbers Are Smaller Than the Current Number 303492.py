# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res = []
        sortedNums = sorted(nums)

        for num in nums:
            for i in range(len(nums)):
                if num <= sortedNums[i]:
                    res.append(i)
                    break

        return res

        