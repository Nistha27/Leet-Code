class ProductOfNumbers(object):

    def __init__(self):
        self.prefix_products = [1]  # Initialize prefix products with 1
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefix_products = [1]  # Reset on zero
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefix_products):
            return 0  # If k extends beyond last zero, return 0
        return self.prefix_products[-1] // self.prefix_products[-(k + 1)]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)