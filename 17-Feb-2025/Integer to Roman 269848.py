# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
    def intToRoman(self, num):
        rmap = [
            (1000, 'M'), 
            (900, 'CM'), 
            (500, 'D'), 
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        res = ""

        for val, symbol in rmap:
            if num >= val:
                a = num // val
                num -= (val*a)
                res += symbol*a

        return res