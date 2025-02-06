# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)

        if k > n:
            while k > n:
                k -= n

            for _ in range(k):
                nums.insert(0, nums[-1])
                nums.pop()

            return nums
        else:
            i = n - k
            nums[:] = nums[i:] + nums[:i]
            return nums