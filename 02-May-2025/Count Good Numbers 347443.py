# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution(object):
    def countGoodNumbers(self, n):
        return (pow(5, (n+1)//2, pow(10, 9) + 7) * pow(4, n//2, pow(10, 9) + 7)) % (pow(10, 9) + 7)