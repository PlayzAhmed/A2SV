# Problem: Check Equal Arrays - https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

class Solution:
    def checkEqual(self, a, b):
        a.sort()
        b.sort()
        
        return a == b