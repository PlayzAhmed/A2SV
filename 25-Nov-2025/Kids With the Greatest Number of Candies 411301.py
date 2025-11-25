# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        mx = max(candies)
        ans = []

        for x in candies:
            if x + extraCandies >= mx:
                ans.append(True)
            else:
                ans.append(False)

        return ans
        