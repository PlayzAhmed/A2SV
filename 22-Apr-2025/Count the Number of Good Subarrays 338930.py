# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution(object):
    def countGood(self, nums, k):
        n = len(nums)
        res = 0
        freq = defaultdict(int)
        pairs = 0
        l = 0

        for r in range(n):
            pairs += freq[nums[r]]
            freq[nums[r]] += 1

            while pairs - (freq[nums[l]] - 1) >= k:
                freq[nums[l]] -= 1
                pairs -= freq[nums[l]]
                l += 1

            if pairs >= k:
                res += l + 1

        return res
