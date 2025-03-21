# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution(object):
    def totalFruit(self, fruits):
        basket = defaultdict(int)
        l = 0
        m = 0
        for r in range(len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1

            m = max(m, r - l + 1)
        return m