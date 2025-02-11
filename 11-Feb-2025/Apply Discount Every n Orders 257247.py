# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier(object):

    def __init__(self, n, discount, products, prices):
        self.n = n
        self.discount = float(discount)
        self.prices = {products[i]:prices[i] for i in range(len(products))}
        self.customer = 0
        

    def getBill(self, product, amount):
        bill = 0.0
        self.customer += 1

        for i in range(len(product)):
            bill += self.prices[product[i]] * amount[i]

        if self.customer % self.n == 0:
            return bill * ((100 - self.discount) / 100)
        
        return bill
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)