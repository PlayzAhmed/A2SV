# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        k = len(s1)
        s1 = Counter(s1)
        
        for i in range(len(s2)-k+1):
            temp = Counter(s2[i:i+k])
            if temp == s1:
                return True


        return False


        