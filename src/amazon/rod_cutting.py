'''
rod cutting problem
rod of length = 5
prices of different lengths
1 = 2$
2 = 3
3 = 1
4 = 5
5 = 4

solution:
define a variable named "prices" in the initialization of the class to hold the prices.
 K: length, v: function get_price
when try to get price by length call dict['length'] = get_price

time complexity : O(n^2)
'''

import sys


class Solution:
    def __init__(self, prices):
        self.prices = prices
        self.cache = dict()

    def cut_rod(self, n):
        if n <= 0:
            return 0
        if n in self.cache:
            return self.cache[n]
        max_val = -sys.maxsize - 1

        for i in range(n):
            max_val = max(max_val, self.prices[i] + self.cut_rod(n - i - 1))

        self.cache[n] = max_val
        return max_val


s = Solution([1, 5, 8, 9, 10, 17, 17, 20])
print(f"best price is {s.cut_rod(8)}")


class Knapsack:
    def __init__(self, prices):
        self.prices = prices
        self.cache = []

    def cut_rod(self, n):
        pass
        # if n <= 0:
        #     return 0
        #
        # if len(self.prices)
