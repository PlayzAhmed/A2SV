# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution(object):
    def rowAndMaximumOnes(self, mat):
        maxOnes = 0
        index = 0

        for row in range(len(mat)):
            maxOne = 0
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    maxOne += 1

            if maxOne > maxOnes:
                maxOnes = maxOne
                index = row

        return [index, maxOnes]

