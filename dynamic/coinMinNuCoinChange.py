#You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

#from each denominations we may have unlimited resources

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = set(coins)
        a = [float('inf') for i in range(amount + 1)]

        a[0] = 0
        for i in range(1, len(a)):
            minCo = float('inf')
            for co in coins:
                if (i - co >= 0):
                    minCo = min(a[i - co] + 1, minCo)
            a[i] = minCo
        return a[-1] if a[-1] != float('inf') else -1
#O(coins*amount)
#a[i]: minimum numbeer of coins we need to make amount i