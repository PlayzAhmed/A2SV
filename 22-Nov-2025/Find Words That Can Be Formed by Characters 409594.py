# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution(object):
    def countCharacters(self, words, chars):
        freq = [0] * 26
        count = 0

        for x in chars:
            freq[ord(x) - ord('a')] += 1

        for w in words:
            word_freq = [0]*26
            is_valid = True
            for l in w:
                word_freq[ord(l) - ord('a')] += 1

            for i in range(len(word_freq)):
                if word_freq[i] > freq[i]:
                    is_valid = False
                    break

            if is_valid:
                count += len(w)
        
        return count
