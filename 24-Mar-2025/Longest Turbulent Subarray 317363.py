# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        mx = 1
        greater = None
        l = 0

        for r in range(n-1):
            if greater == None and arr[r] != arr[r+1]:
                greater = arr[r] > arr[r+1]
                l = r - 1
                mx = max(mx, r - l + 1)
            elif arr[r] == arr[r+1]:
                greater = None
            elif greater != None and arr[r] != arr[r+1]:
                if (arr[r] > arr[r+1]) == greater:
                    l = r - 1
                
                greater = arr[r] > arr[r+1]
                mx = max(mx, r - l + 1)

        return mx