# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        n = len(intervals)

        intervals = sorted(intervals, key=min)

        res = [intervals[0]]

        for i in range(1, n):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        
        return res