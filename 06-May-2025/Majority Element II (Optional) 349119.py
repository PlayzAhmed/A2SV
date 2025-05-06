# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution(object):
    def majorityElement(self, nums):
        res = []
        n = len(nums)
        nums = Counter(nums)

        for num, freq in nums.items():
            if freq > n/3:
                res.append(num)

        return res