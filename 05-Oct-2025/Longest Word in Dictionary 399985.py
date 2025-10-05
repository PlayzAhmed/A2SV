# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution(object):
    def longestWord(self, words):
        wordset = set(words)
        ans = ""
        words.sort(reverse=True, key=len)

        for word in words:
            f = True
            for i in range(1,len(word)):
                if word[:i] not in words:
                    f = False
                    break

            if f:
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word

            if len(word) < len(ans):
                break

        return ans