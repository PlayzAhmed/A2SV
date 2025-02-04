# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution(object):
    def rearrangeArray(self, nums):
        p, n, res = [], [], []

        for x in nums:
            if x > 0:
                p.append(x)
            else:
                n.append(x)

        for i in range(len(p)):
            res.append(p[i])
            res.append(n[i])

        return res

        