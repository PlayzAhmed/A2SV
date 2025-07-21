# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        for i in range(len(flowerbed)):
            both = True
            if (i - 1 >= 0 and flowerbed[i-1]) or flowerbed[i]:
                both = False
            if (i + 1 < len(flowerbed) and flowerbed[i+1]) or flowerbed[i]:
                both = False

            if both: 
                flowerbed[i] = 1
                n -= 1

        return n <= 0
        