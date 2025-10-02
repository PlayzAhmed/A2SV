# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution(object):
    def topKFrequent(self, words, k):
        words = [(-x, word) for word, x in Counter(words).items()]
        heapify(words)
        return [heappop(words)[1] for _ in range(k)]
        