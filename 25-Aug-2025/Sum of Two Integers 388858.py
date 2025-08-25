# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution(object):
    def getSum(self, a, b):
        if a < 0 or b < 0:
            return a + b

        i = 0
        carry = 0
        ans = 0

        while a or b or carry:
            lsb_a = a & 1
            lsb_b = b & 1

            if lsb_a == 0 and lsb_b == 0:
                if carry:
                    carry -= 1
                    ans += pow(2, i)
            elif lsb_a ^ lsb_b:
                if not carry:
                    ans += pow(2, i)
            elif lsb_a and lsb_b:
                if carry:
                    ans += pow(2, i)
                else:
                    carry += 1

            i += 1
            a >>= 1
            b >>= 1

        return ans