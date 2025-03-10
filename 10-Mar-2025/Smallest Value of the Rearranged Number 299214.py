# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution(object):
    def smallestNumber(self, num):
        num = list(str(num))

        if num[0] == "-":
            num = list(map(int, num[1:]))
            num.sort(reverse=True)
            num = list(map(str, num))
            return int("".join(num)) * -1
        else: 
            num = list(map(int, num))
            num.sort()
            num = list(map(str, num))
            if num[0] == "0":
                for i in range(len(num)):
                    if num[i] != "0":
                        num[0], num[i] = num[i], num[0]
                        break

            return int("".join(num))