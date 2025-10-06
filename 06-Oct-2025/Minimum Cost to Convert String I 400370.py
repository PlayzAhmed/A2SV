# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        graph = defaultdict(list)
        dist = [[float("inf") for _ in range(26)] for _ in range(26)]
        ans = 0

        for i in range(len(original)):
            graph[original[i]].append((changed[i], cost[i]))
        
        def shortestPath(x, y):
            heap = []
            dist = {x:0}
            seen = set()
            heappush(heap, (0, x))

            while heap:
                cost, x = heappop(heap)

                if x == y:
                    return cost

                if x in seen:
                    continue

                seen.add(x)

                for node, w in graph[x]:
                    newCost = w + cost

                    if node not in dist or newCost < dist[node]:
                        dist[node] = newCost
                        heappush(heap, (newCost, node))

            return -1

        for i in range(len(source)):
            if source[i] == target[i]:
                continue

            x, y = ord(source[i])-97, ord(target[i])-97
            cost = dist[x][y]

            if dist[x][y] == float("inf"):
                cost = shortestPath(source[i], target[i])
                dist[x][y] = cost

            if cost == -1:
                return -1
            ans += cost

        return ans