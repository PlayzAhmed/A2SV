# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution(object):
    def __init__(self):
        self.d = {0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
            }

    def numberToWords(self, num):
        if 100 > num:
            return self.tensHelper(num)
        elif 1000 > num:
            return self.hundredsHelper(num)
        elif 1000000 > num:
            return self.thousandsHelper(num)
        elif 1000000000 > num:
            return self.millionsHelper(num)
        else:
            return self.billionsHelper(num)

    def tensHelper(self, num):
        if num in self.d:
            return self.d[num]
        tens = (num // 10) * 10
        units = num - tens
        return self.d[tens] + " " + self.d[units]

    def hundredsHelper(self, num):
        hundreds = num // 100
        if num % 100:
            return self.d[hundreds] + " " + self.d[100] + " " + self.tensHelper(num - hundreds * 100)
        else:
            return self.d[hundreds] + " " + self.d[100]

    def thousandsHelper(self, num):
        thousands = num // 1000
        thousandsString = ""
        if thousands < 10:
            thousandsString = self.d[thousands] + " " + self.d[1000]
        elif 9 < thousands < 100:
            thousandsString = self.tensHelper(thousands) + " " + self.d[1000]
        elif 99 < thousands < 1000:
            thousandsString = self.hundredsHelper(thousands) + " " + self.d[1000]

        rest = num - thousands * 1000

        if 0 < rest < 10:
            thousandsString += " " + self.d[rest]
        elif 9 < rest < 100:
            thousandsString += " " + self.tensHelper(rest)
        elif 99 < rest < 1000:
            thousandsString += " " + self.hundredsHelper(rest)

        return thousandsString

    def millionsHelper(self, num):
        millions = num // 1000000
        millionsString = ""

        if millions < 10:
            millionsString = self.d[millions] + " " + self.d[1000000]
        elif 9 < millions < 100:
            millionsString = self.tensHelper(millions) + " " + self.d[1000000]
        elif 99 < millions < 1000:
            millionsString = self.hundredsHelper(millions) + " " + self.d[1000000]
        elif 999 < millions < 1000000:
            millionsString = self.thousandsHelper(millions) + " " + self.d[1000000]

        rest = num - millions * 1000000

        if 0 < rest < 10:
            millionsString += " " + self.d[rest]
        elif 9 < rest < 100:
            millionsString += " " + self.tensHelper(rest)
        elif 99 < rest < 1000:
            millionsString += " " + self.hundredsHelper(rest)
        elif 999 < rest < 1000000:
            millionsString += " " + self.thousandsHelper(rest)

        return millionsString

    def billionsHelper(self, num):
        billions = num // 1000000000
        billionsString = ""

        if billions < 10:
            billionsString = self.d[billions] + " " + self.d[1000000000]
        elif 9 < billions < 100:
            billionsString = self.tensHelper(billions) + " " + self.d[1000000000]
        elif 99 < billions < 1000:
            billionsString = self.hundredsHelper(billions) + " " + self.d[1000000000]
        elif 999 < billions < 1000000:
            billionsString = self.thousandsHelper(billions) + " " + self.d[1000000000]
        elif 9999 < billions < 1000000000:
            billionsString = self.millionsHelper(billions) + " " + self.d[1000000000]

        rest = num - billions * 1000000000

        if 0 < rest < 10:
            billionsString += " " + self.d[rest]
        elif 9 < rest < 100:
            billionsString += " " + self.tensHelper(rest)
        elif 99 < rest < 1000:
            billionsString += " " + self.hundredsHelper(rest)
        elif 999 < rest < 1000000:
            billionsString += " " + self.thousandsHelper(rest)
        elif 9999 < rest < 1000000000:
            billionsString += " " + self.millionsHelper(rest)

        return billionsString