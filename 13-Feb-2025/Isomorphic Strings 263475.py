# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        dic = {}
        dit = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i]

            if t[i] not in dit:
                dit[t[i]] = s[i]
            

        string1 = ""
        string2 = ""

        for i in range(len(s)):
            string1 += dic[s[i]]
            string2 += dit[t[i]]

        return string1 == t and string2 == s

        