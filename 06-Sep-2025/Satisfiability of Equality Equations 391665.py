# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution(object):
    def equationsPossible(self, equations):
        parent = [i for i in range(26)]
        rank = [1] * 26
        equations.sort(key=lambda x:x[1], reverse=True)
        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[parent[parent[n]]])

            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 != p2:
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]

        for eq in equations:
            x, y = ord(eq[0]) - 97, ord(eq[-1]) - 97

            if eq[1] == "!" and find(x) == find(y): return False
            if eq[1] == "=": union(x, y)
            
        return True