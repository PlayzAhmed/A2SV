# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution(object):
    def minimumReplacement(self, nums):
        ans = 0
        prev = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > prev:
                k = (nums[i] + prev - 1) // prev
                ans += k - 1
                prev = nums[i] // k
            else:
                prev = nums[i]

        return ans