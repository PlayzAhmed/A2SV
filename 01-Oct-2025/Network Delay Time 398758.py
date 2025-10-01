# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        cost = {node:float("inf") for node in range(1, n+1)}
        cost[k] = 0
        heap = []
        heappush(heap, (0, k))
        seen = set()

        for u, v, t in times:
            graph[u].append((v, t))

        while heap:
            time, parent = heappop(heap)

            if parent in seen: continue

            seen.add(parent)

            for child, t in graph[parent]:
                newTime =  time + t

                if newTime < cost[child]:
                    cost[child] = newTime
                    heappush(heap, (newTime, child))

        ans = -1

        for node, time in cost.items():
            ans = max(ans, time)


        return ans if ans != -1 and ans != float("inf") else -1
        