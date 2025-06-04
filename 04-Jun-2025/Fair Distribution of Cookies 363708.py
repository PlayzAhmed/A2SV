# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution(object):
    def distributeCookies(self, cookies, k):
        res = [float('inf')]
        c = [0] * k
        n = len(cookies)

        def backtrack(children, i=0):
            if i >= n:
                res[0] = min(max(children), res[0])
                return
            
            if res[0] <= max(children):
                return

            for j in range(k):
                children[j] += cookies[i]
                backtrack(children, i+1)
                children[j] -= cookies[i]

        backtrack(c)
        return res[0]

        