# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode(object):
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for ch in word:
            idx = ord(ch) - 97

            if not cur.children[idx]:
                cur.children[idx] = TrieNode()

            cur = cur.children[idx]

        cur.end = True

    def prefix(self, word):
        cur = self.root

        for ch in word:
            idx = ord(ch) - 97

            if not cur.children[idx]:
                return []
            
            cur = cur.children[idx]

        return cur

    def suggest(self, node, word, ans):
        if len(ans) == 3 or not node:
            return []

        if node.end:
            ans.append(word)

        for i in range(26):
            if node.children[i]:
                self.suggest(node.children[i], word+chr(97+i), ans)

        return ans

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        word = ""
        ans = []

        for product in products:
            trie.insert(product)

        for ch in searchWord:
            word += ch
            temp = trie.suggest(trie.prefix(word), word, [])
            ans.append(temp if temp else [])

        return ans