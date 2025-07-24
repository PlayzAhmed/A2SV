# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution(object):
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)
        income = [0] * n
        q = deque()
        ans = [i for i in range(n)]
        
        for a, b in richer:
            graph[a].append(b)
            income[b] += 1

        for i in range(n):
            if not income[i]: q.append(i)

        while q:
            parent = q.popleft()

            for node in graph[parent]:
                if quiet[node] > quiet[parent]:
                    quiet[node] = quiet[parent]
                    ans[node] = ans[parent]
                income[node] -= 1
                
                if not income[node]: q.append(node)

        return ans