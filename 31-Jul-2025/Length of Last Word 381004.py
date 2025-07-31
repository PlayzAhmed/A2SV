# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split()

        return len(s[-1])