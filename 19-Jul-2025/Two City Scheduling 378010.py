# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution(object):
    def twoCitySchedCost(self, costs):
        heap = []
        ans = 0
        costs.sort(key=lambda x: x[0]-x[1])

        for i in range(len(costs)//2):
            a, b = costs[i]
            ans += a
            heappush(heap, (b, -a))

        for i in range(len(costs)//2, len(costs)):
            a, b = costs[i]
            y, x = heap[0]

            if ans + b > ans + y + a + x:
                heapreplace(heap, (b, -a))
                ans += y + a + x
            else:
                ans += b
        
        return ans