# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        return min(numOnes, k) - min(numNegOnes, k - (min(numOnes, k) + min(numZeros, k-min(numOnes, k))))
        