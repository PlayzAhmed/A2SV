# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        res = ""
        preSum = [0] * (n+1)

        for shift in shifts:
            if shift[2] == 0:
                preSum[shift[0]] -= 1
                preSum[shift[1]+1] += 1
            else:
                preSum[shift[0]] += 1
                preSum[shift[1]+1] -= 1

        for i in range(1, len(preSum)):
            preSum[i] += preSum[i-1]

        for i in range(n):
            res += chr((((ord(s[i])-97)+preSum[i]+26)%26)+97)

        return res