# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution(object):
    def maxOperations(self, nums, k):
        p = 0
        nums = Counter(nums)

        for x in nums.keys():
            if nums[k-x] > 0 and nums[x] > 0:
                c = 0
                if x == k / 2:
                    c = floor(nums[x]/2)
                else:
                    c = min(nums[x], nums[k-x])

                p += c
                nums[x] -= c
                nums[k-x] -= c


        return int(p)
        