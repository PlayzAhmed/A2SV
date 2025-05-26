# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution(object):
    def isLongPressedName(self, name, typed):
        index = 0
        n = len(typed)
        m = len(name)

        for i in range(n):
            if index >= m:
                index -= 1
            if i > 0 and typed[i] == typed[i-1] and typed[i] != name[index]:
                continue

            if typed[i] == name[index]:
                index += 1
            else:
                return False

        
        return True if index == m else False
        