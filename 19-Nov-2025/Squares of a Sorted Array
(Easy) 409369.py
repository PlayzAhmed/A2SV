# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, nums):
        ans = []
        l = -1

        for i in range(len(nums)):
            if nums[i] < 0:
                l = i
            else:
                break

        r = l + 1

        while True:
            if l >= 0 and r < len(nums):
                if nums[l] == nums[r]:
                    ans.append(pow(nums[l], 2))
                    ans.append(pow(nums[l], 2))
                    l -= 1
                    r += 1
                elif abs(nums[l]) > nums[r]:
                    ans.append(pow(nums[r], 2))
                    r += 1
                else:
                    ans.append(pow(nums[l], 2))
                    l -= 1
            elif r < len(nums):
                ans.append(pow(nums[r], 2))
                r += 1
            elif l >= 0:
                ans.append(pow(nums[l], 2))
                l -= 1
            else:
                break
        
        return ans