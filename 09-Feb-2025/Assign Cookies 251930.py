# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution(object):
    def findContentChildren(self, g, s):
        cookiesNum = len(s)
        childrenNum = len(g)
        if cookiesNum == 0:
            return 0
        
        g.sort()
        s.sort()

        counter = 0
        cookie = cookiesNum - 1
        child = childrenNum - 1

        while cookie >= 0 and child >= 0:
            if s[cookie] >= g[child]:
                counter += 1
                cookie -= 1
                child -= 1
            else:
                child -= 1

        return counter