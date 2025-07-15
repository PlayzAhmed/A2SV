# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution(object):
    def lemonadeChange(self, bills):
        q = [0, 0]
        pocket = {
            5: 0,
            10: 0
        }
        
        def change_10(amount):
            if pocket[5] >= amount: 
                pocket[5] -= amount
                return True
            return False

        def change_20(amount):
            if pocket[5] >= amount and pocket[10] >= amount:
                pocket[5] -= amount
                pocket[10] -= amount
                return True
            elif pocket[5] and pocket[5] >= amount + (amount - pocket[10]) * 2:
                pocket[5] -= amount + (amount - pocket[10]) * 2
                pocket[10] = 0
                return True
            return False

        for x in bills:
            if x == 5: pocket[5] += 1
            elif x == 10:
                if change_10(1): pocket[10] += 1
                else: q[0] += 1
            else:
                if not change_20(1): q[1] += 1

        if not q[0] and not q[1]: return True
        return False

        