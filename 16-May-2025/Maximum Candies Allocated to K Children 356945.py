# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution(object):
    def maximumCandies(self, candies, k):
        left, right = 1, max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            count = 0

            for candy in candies:
                count += candy // mid

            if count < k:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid
            
        return ans
        