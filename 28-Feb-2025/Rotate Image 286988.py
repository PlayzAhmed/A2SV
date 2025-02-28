# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
        