# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution(object):
    def findChampion(self, n, edges):
        ans = set()

        for i in range(n):
            ans.add(i)

        for _, v in edges:
            if v in ans:
                ans.remove(v)

        if len(ans) == 1:
            for x in ans:
                return x
        return -1
        

