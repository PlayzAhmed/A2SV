# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution(object):
    def duplicateZeros(self, arr):
        skip = -1
        n = len(arr)
        def shift(x):
            for i in range(n-1, x, -1):
                arr[i] = arr[i-1]

        for i in range(n):
            if arr[i] == 0 and i != skip:
                skip = i+1
                shift(i)
        