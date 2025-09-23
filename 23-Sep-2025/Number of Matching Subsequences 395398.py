# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]

        current.end = True

    def search(self, word):
        current = self.root

        for ch in word:
            while current.children and ch not in current.children:
                if not current.children.values():
                    return False
                for child in current.children.values():
                    current = child

            if not current.children:
                return False
            
            current = current.children[ch]

        return True

class Solution(object):
    def numMatchingSubseq(self, s, words):
        root = Trie()
        root.insert(s)
        ans = 0
        cache = {}

        for word in words:
            if word in cache and cache[word] == False:
                continue
                
            if word in cache or root.search(word):
                cache[word] = True
                ans += 1
            else:
                cache[word] = False

        return ans