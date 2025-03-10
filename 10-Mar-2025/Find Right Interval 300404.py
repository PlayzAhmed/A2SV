# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution(object):
    def findRightInterval(self, intervals):
        n = len(intervals)
        sorted_intervals = sorted((interval[0], i) for i, interval in enumerate(intervals))
        res = []

        for interval in intervals:
            idx = bisect.bisect_left(sorted_intervals, (interval[1],))
            if idx < n:
                res.append(sorted_intervals[idx][1])
            else:
                res.append(-1)
        return res