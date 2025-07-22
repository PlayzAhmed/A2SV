# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        income = [0] * numCourses
        ans = []
        q = deque()
        visited = set()

        for a, b in prerequisites:
            graph[b].append(a)

            income[a] += 1

        for i in range(numCourses):
            if not income[i]:
                q.append(i)

        while q:
            node = q.popleft()

            if node in visited: continue

            visited.add(node)
            ans.append(node)

            for nei in graph[node]:
                income[nei] -= 1
                if not income[nei]: q.append(nei)

        if len(ans) == numCourses:
            return ans

        return []
