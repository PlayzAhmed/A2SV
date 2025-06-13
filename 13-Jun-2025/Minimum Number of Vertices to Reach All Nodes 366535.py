# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        nodes = [0] * n
        ans = []

        for x, y in edges:
            nodes[y] += 1
        
        for i in range(n):
            if nodes[i] == 0: ans.append(i)

        return ans
        