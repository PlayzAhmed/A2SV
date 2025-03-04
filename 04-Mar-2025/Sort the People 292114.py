# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):
        n = len(names)

        for i in range(n-1):
            is_sorted = True
            for j in range(n-1):
                if heights[j] < heights[j+1]:
                    is_sorted = False
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]

            if is_sorted:
                return names

        return names
        