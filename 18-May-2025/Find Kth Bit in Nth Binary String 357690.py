# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution(object):
    def findKthBit(self, n, k):
        return self.generateString(n, "0")[k-1]


    def generateString(self, n, s):
        if n == 1:
            return s
        return self.generateString(n-1, s + "1" + self.invert(s))

    def invert(self, s):
        s = list(s)
        for i in range(len(s)):
            if s[i] == "1":
                s[i] = "0"
            else:
                s[i] = "1"

        return "".join(reversed(s))

        