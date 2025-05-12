# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        res = []

        for x in nums1.keys():
            if x in nums2:
                res.extend([x] * min(nums2[x], nums1[x]))

        return res

        