# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        prev = [float("inf") for _ in range(n)]
        prev[src] = 0

        for _ in range(k+1):
            cur = prev[:]

            for f, t, p in flights:
                cur[t] = min(cur[t], prev[f]+p)

            prev = cur[:]

        return prev[dst] if prev[dst] != float("inf") else -1