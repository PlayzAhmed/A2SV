# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return [left+1, right+1]
        