# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution(object):
    def convertToTitle(self, columnNumber):
        dic = {i:chr(64+i) for i in range(1, 26)}
        dic[0] = "Z"
        ans = ""

        while columnNumber > 0:
            index = columnNumber % 26
            ans += dic[index]
            if columnNumber < 27:
                break
            if index == 0:
                columnNumber -= 1
            columnNumber //= 26

        return ans[::-1]