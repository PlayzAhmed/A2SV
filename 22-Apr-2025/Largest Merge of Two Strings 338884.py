# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution(object):
    def largestMerge(self, word1, word2):
        res = ""
        p1 = 0
        p2 = 0
        n = len(word1)
        m = len(word2)

        while p1 < n and p2 < m:
            if word1[p1] > word2[p2]:
                res += word1[p1]
                p1 += 1
            elif word1[p1] < word2[p2]:
                res += word2[p2]
                p2 += 1
            else:
                i, j = p1, p2

                while i < n and j < m and word1[i] == word2[j]:
                    i += 1
                    j += 1

                    if i >= n and j >= m:
                        i -= 1
                        j -= 1
                        break

                    if i >= n:
                        i -= 1
                    if j >= m:
                        j -= 1

                if word1[i] > word2[j]:
                    res += word1[p1]
                    p1 += 1
                else:
                    res += word2[p2]
                    p2 += 1


        return res + ''.join(word1[p1:]) + ''.join(word2[p2:])