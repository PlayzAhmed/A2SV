# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        a = [(row, col) for row in range(n) for col in range(n) if img1[row][col]]
        b = [(row, col) for row in range(n) for col in range(n) if img2[row][col]]
        counter = Counter((rowA - rowB, colA - colB) for rowA, colA in a for rowB, colB in b)
        return max(counter.values() or [0])