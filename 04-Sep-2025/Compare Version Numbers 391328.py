# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        i = 0
        j = 0

        while i < len(version1) or j < len(version2):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[j]) if j < len(version2) else 0

            if v1 < v2: return -1
            if v1 > v2: return 1

            i += 1
            j += 1
        return 0