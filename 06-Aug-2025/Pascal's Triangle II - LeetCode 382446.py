# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        ans = [1]

        for _ in range(rowIndex):
            row = []
            
            for i in range(len(ans)+1):
                a = ans[i-1] if i - 1 >= 0 else 0
                b = ans[i] if i < len(ans) else 0
                row.append(a+b)

            ans = row

        return ans
        