# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution(object):
    def countVowelSubstrings(self, word):
        v = "aeiou"
        n = len(word)
        res = 0
        freq = set()

        for i in range(n):
            freq.clear()
            for j in range(i, n):
                if word[j] not in v:
                    break

                freq.add(word[j])
                if len(freq) == 5:
                    res += 1


        return res