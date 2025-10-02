# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        cache = {}
        for x,y in prerequisites:
            graph[x].append(y)

        def dfs(start, end):
            if start == end: cache[(start, end)] = True
            if (start, end) in cache: return cache[(start, end)]
            
            ans = False

            for node in graph[start]:
                if node == end: cache[(node, end)] = True
                if (node, end) not in cache:
                    cache[(node, end)] = dfs(node, end)

                ans = ans or cache[(node, end)]

            if (start, end) not in cache:
                cache[(start, end)] = ans
                
            return cache[(start, end)]
        
        ans = []

        for x, y in queries:
            ans.append(dfs(x, y))

        return ans