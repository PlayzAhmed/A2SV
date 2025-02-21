# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)

        for i in range(n):
            image[i].reverse()

        for i in range((n)):
            for j in range(n):
                image[i][j] = int(not image[i][j])

        return image
        