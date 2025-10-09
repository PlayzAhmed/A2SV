# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class KMP(object):    
    def LPS(self, target):
        n = len(target)
        lps = [0] * n
        i, j = 0, 1

        while j < n:
            if target[i] == target[j]:
                i += 1
                lps[j] = i
                j += 1
            elif i == 0:
                j += 1
            else:
                i = lps[i - 1]

        return lps

    def search(self, string, target):
        n = len(target)
        m = len(string)

        i = j = 0
        ans = 1
        lps = self.LPS(target)

        while i < m:
            if string[i] == target[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            elif ans < 3:
                j = lps[j-1]
            else:
                return -1

            if j == n:
                return ans
            
            if i == m and j != 0:
                i = 0
                ans += 1
                  
        return -1

class Solution(object):
    def repeatedStringMatch(self, a, b):
        return KMP().search(a, b)