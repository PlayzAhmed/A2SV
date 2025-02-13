# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution(object):
    def majorityElement(self, nums):
        res = []
        n = len(nums)
        nums = Counter(nums)

        for num, freq in nums.items():
            if freq > n/3:
                res.append(num)

        return res
        