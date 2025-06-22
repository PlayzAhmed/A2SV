# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        visited = set()

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(i):
            if i in visited: return False
            if graph[i] == []: return True

            visited.add(i)

            for x in graph[i]:
                if not dfs(x): return False
            
            visited.remove(i)
            graph[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True