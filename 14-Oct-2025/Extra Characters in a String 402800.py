# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.end = True

    def search(self, word, start):
        cur = self.root
        n = len(word)
        ans = []

        for i in range(start, n):
            if word[i] not in cur.children: break
            cur = cur.children[word[i]]
            if cur.end: ans.append(i+1)

        return ans

class Solution(object):
    def minExtraChar(self, s, dictionary):
        trie = Trie()
        ans = [float("inf")]
        cache = {}

        for w in dictionary:
            trie.insert(w)

        def dfs(s, start=0):
            n = len(s)
            if start >= n:
                return 0
            if start in cache:
                return cache[start]
            
            res = 1 + dfs(s, start+1)

            for end in trie.search(s, start):
                res = min(res, dfs(s, end))

            cache[start] = res
            return cache[start]

        return dfs(s)