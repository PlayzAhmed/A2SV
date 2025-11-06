# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution(object):
    def equalFrequency(self, word):
        word = Counter(Counter(word).values())

        if len(word) <= 2:
            word = list(word.items())
            word.sort()
            return (len(word) > 1 and word[1][1] == 1 and word[1][0] - 1 == word[0][0]) or (word[0][1] == 1 and word[0][0] == 1) or (len(word) == 1 and (word[0][1] == 1 or word[0][0] == 1))
        else:
            return False