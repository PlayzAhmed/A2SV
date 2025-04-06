# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        t = 0
        res = 0
        remainder = {0: 1}

        for i in range(len(nums)):
            t += nums[i]
            r = t % k

            if r in remainder:
                res += remainder[r]
                remainder[r] += 1
            else:
                remainder[r] = 1

        return res

        