# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.getSubarray(nums, k) - self.getSubarray(nums, k - 1)

    def getSubarray(self, nums, k):
        n = len(nums)
        l = 0
        res = 0
        freq = defaultdict(int)

        for r in range(n):
            freq[nums[r]] += 1

            while len(freq) > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    freq.pop(nums[l])

                l += 1

            if len(freq) <= k:
                res += r - l + 1


        return res