# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution(object):
    def findJudge(self, n, trust):
        graph = defaultdict(list)
        trust_counter = [0] * (n+1)

        for a, b in trust:
            trust_counter[b] += 1
            graph[a].append(b)

        for i in range(1, n+1):
            if trust_counter[i] == n - 1:
                return i if not graph[i] else -1

        return -1

        