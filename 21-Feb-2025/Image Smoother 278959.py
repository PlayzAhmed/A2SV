# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution():
    def imageSmoother(self, img):
        rows = len(img)
        columns = len(img[0])
        gray_scale = [[0]*columns for _ in range(rows)]
        for row in range(rows):
            for col in range(columns):
                val = 0
                count = 0
                if row - 1 >= 0 and col - 1 >= 0:
                    val += img[row-1][col-1]
                    count += 1
                if row + 1 < rows and col + 1 < columns:
                    val += img[row+1][col+1]
                    count += 1
                if row + 1 < rows and col - 1 >= 0:
                    val += img[row+1][col-1]
                    count += 1
                if row - 1 >= 0 and col + 1 < columns:
                    val += img[row-1][col+1]
                    count += 1
                if row + 1 < rows:
                    val += img[row+1][col]
                    count += 1
                if row - 1 >= 0:
                    val += img[row-1][col]
                    count += 1
                if col + 1 < columns:
                    val += img[row][col+1]
                    count += 1
                if col - 1 >= 0:
                    val += img[row][col-1]
                    count += 1
                
                gray_scale[row][col] = (val+img[row][col]) // (count+1)
        return gray_scale