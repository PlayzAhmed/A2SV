# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution(object):
    def isThree(self, n):
        count = 0

        for i in range(1, n+1):
            if n % i == 0:
                count += 1

        return 3 == count
        