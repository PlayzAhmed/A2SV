# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution(object):
    def maskPII(self, s):
        n = ""
        is_number = not (s[0].isalpha())

        for x in s:
            if is_number:
                if x.isdigit():
                    n += x
            else:
                if x == '@':
                    break
                n += x


        if is_number:
            l = len(n)

            if l == 10:
                return "***-" * 2 + n[l-4:]
            else:
                return "+" + "*" * (l%10) + "-" + "***-" * 2 + n[l-4:]
        else:
            i = s.find('@')
            return n[0].lower() + "*" * 5 + n[-1].lower() + s[i:].lower()

        