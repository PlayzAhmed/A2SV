# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        nums = []
        while True:
            
            temp = 0
            for d in str(n):
                temp += pow(int(d), 2)
            
            if temp == 1:
                return True
            else:
                if temp in nums:
                    return False
                nums.append(temp)
                n = temp
        