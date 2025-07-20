# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution(object):
    def freqAlphabets(self, s):
        ans = [""] * len(s)

        i = len(s) - 1

        while i >= 0:
            if s[i] == "#":
                ans[i] = chr(int(s[i-2] + s[i-1]) + 96)
                i -= 3
            else:
                ans[i] = chr(int(s[i]) + 96)
                i -= 1
        
        return "".join(ans)