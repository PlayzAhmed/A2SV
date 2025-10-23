# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution(object):
    def majorityElement(self, nums):
        freq = defaultdict(int)
        n = len(nums)
        r = n//3
        res = []
        for x in nums:
            freq[x] += 1
            if freq[x] > r and x not in res:
                res.append(x)

        return res
        