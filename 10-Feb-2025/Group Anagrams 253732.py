# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):

        if not strs:
            return [[""]]

        dic = {}

        for string in strs:
            sorted_string = str(sorted(string))

            if sorted_string in dic:
                dic[sorted_string].append(string)
            else:
                dic[sorted_string] = [string]

        res = []

        for x in dic.values():
            res.append(x)

        return res
            
        