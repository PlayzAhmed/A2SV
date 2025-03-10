# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution(object):
    def pancakeSort(self, arr):
        s_arr = sorted(arr)
        end = len(arr)
        res = []

        while s_arr != arr and end > 0:
            j = arr.index(max(arr[:end]))
            if j != 0 and j != end-1:
                arr[:j+1] = arr[:j+1][::-1]
                res.append(j+1)
            if j != end-1: 
                arr[:end] = arr[:end][::-1]
                res.append(end)
            
            end -= 1

        return res