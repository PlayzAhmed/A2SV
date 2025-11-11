# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution(object):
    def shuffle(self, nums, n):
        i = 0
        j = n
        ans = []

        while (i < n):
            ans.extend([nums[i], nums[j]])
            i += 1
            j += 1

        return ans