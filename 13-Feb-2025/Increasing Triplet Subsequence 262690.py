# Problem: Increasing Triplet Subsequence - https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution(object):
    def increasingTriplet(self, nums):
        
        f = pow(2, 31)
        s = pow(2, 31)

        for t in nums:
            print(f, s, t)

            if t <= f:
                f = t
            elif t <= s:
                s = t
            else:
                return True

        return False
        