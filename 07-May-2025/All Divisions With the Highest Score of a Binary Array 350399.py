# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution(object):
    def maxScoreIndices(self, nums):
        n = len(nums)
        freq = defaultdict(list)
        mx = float("-inf")
        for i in range(1, n):
            nums[i] += nums[i-1]

        for i in range(n+1):
            left = nums[i-1] if i > 0 else 0
            right = nums[n-1] - left if i < n else 0

            left = i - left
            freq[left+right].append(i)
            mx = max(mx, left+right)

        return freq[mx]
        
        