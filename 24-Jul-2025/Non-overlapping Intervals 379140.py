# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        ans = 0
        prev = 0

        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                ans += 1
                if intervals[prev][1] > intervals[i][1]:
                    prev = i
            else:
                prev = i

        return ans
        