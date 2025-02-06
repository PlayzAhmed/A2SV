# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        res = []

        e = 0

        for x in nums:
            if x % 2 == 0:
                e += x

        for val, i in queries:
            if nums[i] % 2 == 0:
                e -= nums[i]

            nums[i] = nums[i] + val

            if nums[i] % 2 == 0:
                e += nums[i]

            res.append(e)


        return res