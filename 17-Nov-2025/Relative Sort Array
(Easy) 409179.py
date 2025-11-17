# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        mx, mn = max(arr1), min(arr1)
        freq = [0] * (mx-mn+1)
        res = []

        for num in arr1:
            freq[num-mn] += 1

        for num in arr2:
            res.extend([num]*freq[num-mn])

        for i in range((mx-mn+1)):
            if i+mn not in arr2 and freq[i] > 0:
                res.extend([i+mn]*freq[i])

        return res

            

        