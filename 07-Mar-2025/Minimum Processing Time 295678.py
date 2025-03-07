# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        tasks.sort()
        processorTime.sort(reverse=True)
        max_time = 0

        for i in range(len(processorTime)):
            for j in range(i*4, (i*4)+4):
                max_time = max(max_time, processorTime[i]+tasks[j])

        return max_time

        