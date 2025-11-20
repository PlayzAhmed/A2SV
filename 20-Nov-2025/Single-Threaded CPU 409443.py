# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution(object):
    def getOrder(self, tasks):
        heap = []
        available = []
        ans = []
        
        for i in range(len(tasks)):
            enqueueTime, processingTime = tasks[i]
            heappush(heap, [enqueueTime, processingTime, i])

        curTime = heap[0][0]
        def takeTasks(curTime):
            while heap and heap[0][0] <= curTime:
                if heap[0][0] <= curTime:
                    _, processingTime, i = heappop(heap)
                    heappush(available, [processingTime, i])

        def doTasks(curTime):
            while available:
                processingTime, i = heappop(available)
                curTime += processingTime
                ans.append(i)
                if heap: takeTasks(curTime)

        while heap or available:
            takeTasks(curTime)
            doTasks(curTime)
            if heap: curTime = heap[0][0]

        return ans