# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        n = len(s)
        dic = {indices[i]:s[i] for i in range(n)}
        res = ""

        for i in range(n):
            res += dic[i]

        return res
        