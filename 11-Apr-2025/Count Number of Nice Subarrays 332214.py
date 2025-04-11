# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        nums[0] = nums[0]%2
        freq = defaultdict(int)
        freq[nums[0]] += 1
        freq[0] += 1
        res = freq[nums[0]-k]
        for i in range(1, n):
            nums[i] = (nums[i]%2) + nums[i-1]
            freq[nums[i]] += 1
            res += freq[nums[i]-k]

        return res