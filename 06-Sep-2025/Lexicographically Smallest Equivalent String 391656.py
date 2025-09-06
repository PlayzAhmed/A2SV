# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        n = len(s1)
        parent = [i for i in range(26)]
        ans = ""

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])

            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 != p2:
                if p1 < p2:
                    parent[p2] = p1
                else:
                    parent[p1] = p2

        for i in range(n):
            n1 = ord(s1[i]) - 97
            n2 = ord(s2[i]) - 97
            union(n1, n2)

        for x in baseStr:
            n = ord(x) - 97
            ans += chr(find(n) + 97)

        return ans