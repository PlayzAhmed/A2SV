# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        last_num = nums[0]
        last_index = 1

        for i in range(1, len(nums)):
            if last_num == nums[i]:
                nums[i] = "_"
            else:
                last_num = nums[i]
                if last_index == i:
                    last_index += 1
                    continue
                nums[last_index], nums[i]  = nums[i], "_"
                last_index += 1

        
        return last_index