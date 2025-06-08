# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution(object):
    def isAdditiveNumber(self, num):
        def dfs(n1, n2, start):
            if (len(n1) > 1 and n1[0] == "0") or (len(n2) > 1 and n2[0] == "0"): return False

            target = int(n1) + int(n2)

            for i in range(start+1, len(num)+1):
                n3 = num[start:i]
                if int(n3) == target: return dfs(n2, n3, i) if i < len(num) else True
                elif int(n3) > target: return False
                elif n3[0] == "0": return False
            return False

        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                if dfs(num[:i], num[i:j], j): return True

        return False