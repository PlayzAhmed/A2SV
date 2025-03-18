# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution(object):
    def findMaxAverage(self, nums, k):
        s = float(sum(nums[0:k]))
        k = float(k)
        avg = s/k

        for i in range(1, len(nums)-int(k)+1):
            s -= nums[i-1]
            s += nums[i+int(k)-1]
            avg = max(avg, s/k)

        return avg
        