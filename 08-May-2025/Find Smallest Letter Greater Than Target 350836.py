# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        n = len(letters)
        left, right = 0, n-1
        i = 0
        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                i = mid
                right = mid - 1

        return letters[i]
        