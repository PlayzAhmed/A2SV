# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution(object):
    def longestSquareStreak(self, nums):
        nums = Counter(nums)

        streak = -1

        for i in nums.keys():
            count = 1
            num = i

            while pow(num, 2) in nums:
                num = pow(num, 2)
                count += 1

            if count > 1:
                streak = max(streak, count)
            
            if streak == 5:
                return 5

        return streak

        