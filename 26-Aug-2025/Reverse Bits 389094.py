# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution(object):
    def reverseBits(self, n):
        ans = 0

        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1

        return ans