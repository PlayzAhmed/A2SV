# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        counter = 0
        for w in words:
            is_allowed = True
            for x in set(w):
                if x not in allowed:
                    is_allowed = False
                    break
            if is_allowed:
                counter += 1

        return counter