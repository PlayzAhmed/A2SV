# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution(object):
    def countDistinctIntegers(self, nums):
        for i in range(len(nums)):
            nums.append(int("".join(reversed(str(nums[i])))))
        
        return len(set(nums))