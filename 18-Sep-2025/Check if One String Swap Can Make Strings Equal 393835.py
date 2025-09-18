# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2: return True

        count = 0
        p1 = set()
        p2 = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                p1.add(s1[i])
                p2.add(s2[i])

        if count == 2 and len(p1) == 2 and p1 == p2:
            return True
        else:
            return False
        