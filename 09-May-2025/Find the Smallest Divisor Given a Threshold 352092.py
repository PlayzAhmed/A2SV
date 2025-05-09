# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        left = 1
        right = pow(10, 9) + 1
        ans = -1

        while left <= right:
            mid = (right + left) // 2
            s = 0

            for n in nums:
                n = float(n) / float(mid)
                s += math.ceil(n)

            if s > threshold:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid

        return ans