# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution(object):
    def sortSentence(self, s):
        s = s.split()
        res = ""
        n = len(s)

        for i in range(n):
            for j in range(n):
                if str(i+1) in s[j]:
                    res += s[j][:-1] + " "

        return res.rstrip()

        