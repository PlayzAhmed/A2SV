# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        counter = 0
        n = len(nums1)
        nums = defaultdict(int)

        for i in range(n):
            for j in range(n):
                nums[nums1[i]+nums2[j]] += 1

        for i in range(n):
            for j in range(n):
                    counter += nums[-(nums4[i]+nums3[j])]

        return counter
        