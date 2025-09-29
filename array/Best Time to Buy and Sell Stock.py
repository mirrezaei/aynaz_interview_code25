#Say you have an array for which the ith element is the price of a given stock on day i.

#If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

#Note that you cannot sell a stock before you buy one.

import sys
#  idea is that we start from the begining of the array and keep track of the minimum price we can but: m
# and then we compute the profit at each step by considering the current minimum we have


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('-inf')
        ind = sys.maxint
        pro = 0
        for i in range(len(prices)):
            if (-prices[i] > buy):
                buy = -prices[i]
                ind = i
            if (i > ind and prices[i] + buy > pro):
                pro = prices[i] + buy
        return pro

    def maxProfit(self, prices): # best approach
        """
        :type prices: List[int]
        :rtype: int
        """
        pro = 0
        if (len(prices) > 1):
            m = prices[0]# m is the minimum value we can buy so far
        for i in range(1, len(prices)):
            if (prices[i] - m > pro):
                pro = prices[i] - m
            m = min(m, prices[i])

        return pro



s=Solution()
prices =[7,1,5,3,6,4]
s.maxProfit(prices)

#2025
