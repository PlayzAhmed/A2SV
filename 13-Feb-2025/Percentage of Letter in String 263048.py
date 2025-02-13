# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution(object):
    def percentageLetter(self, s, letter):
        n = len(s)
        s = Counter(s)

        return int(float(s[letter])/float(n) * 100)
        