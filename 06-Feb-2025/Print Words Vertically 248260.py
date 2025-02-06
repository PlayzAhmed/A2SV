# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution(object):
    def printVertically(self, s):
        s = s.split()
        n = len(max(s, key=len))
        res = [""]*n

        for i in range(n):

            for x in s:
                try:
                    res[i] += x[i]
                except IndexError:
                    res[i] += " "

            res[i] = res[i].rstrip()
        
        return res
        