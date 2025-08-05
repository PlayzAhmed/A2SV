# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):
    def generate(self, numRows):
        ans = [[1]]

        for _ in range(1, numRows):
            row = []
            
            for i in range(len(ans[-1])+1):
                a = ans[-1][i-1] if i - 1 >= 0 else 0
                b = ans[-1][i] if i < len(ans[-1]) else 0
                row.append(a+b)

            ans.append(row)

        return ans
        