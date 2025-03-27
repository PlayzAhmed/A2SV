# Problem: Maximum Sum of Distinct Subarrays With Length K - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        freq = defaultdict(int)
        mx = 0
        cur = 0
        
        for i in range(k):
            freq[nums[i]] += 1
            cur += nums[i]

        if len(freq) == k:
            mx = max(cur, mx)

        for i in range(k, len(nums)):
            freq[nums[i-k]] -= 1
            freq[nums[i]] += 1
            cur -= nums[i-k]
            cur += nums[i]
            if freq[nums[i-k]] == 0: freq.pop(nums[i-k])
            if len(freq) == k:
                mx = max(cur, mx)

        return mx