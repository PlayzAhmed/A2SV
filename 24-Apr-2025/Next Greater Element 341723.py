# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        stack = []
        freq = {}

        for i in range(m):
            if not stack:
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    freq[stack.pop()] = nums2[i]

                stack.append(nums2[i])

        for i in range(n):
            if nums1[i] in freq:
                nums1[i] = freq[nums1[i]]
            else:
                nums1[i] = -1

        return nums1

        