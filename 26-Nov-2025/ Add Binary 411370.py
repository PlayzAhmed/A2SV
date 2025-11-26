# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        carry = 0
        ans = ""

        for i in range(-1, -max(len(a), len(b))-1, -1):
            lsb_a = 0 if i * -1 > len(a) else int(a[i])
            lsb_b = 0 if i * -1 > len(b) else int(b[i])


            if not (lsb_a or lsb_b):
                if carry:
                    carry -=1
                    ans += "1"
                else:
                    ans += "0"
            elif lsb_a ^ lsb_b:
                if carry:
                    ans += "0"
                else:
                    ans += "1"
            else:
                if carry:
                    ans += "1"
                else:
                    carry += 1
                    ans += "0"

        if carry:
            ans += "1"

        return ans[::-1]