# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution(object):
    def superPow(self, a, b):
        n = ""
        for x in b:
            n += str(x)
        b = int(n)

        return pow(a, b, 1337)  