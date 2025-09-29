#You are climbing a stair case. It takes n steps to reach to the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

import numpy as np


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = np.full(n + 1, 0)
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        elif (n == 2):
            return 2
        else:
            a[0] = 0
            a[1] = 1
            a[2] = 2
            for i in range(3, n + 1):
                a[i] = a[i - 1] + a[i - 2]
        return int(a[n])

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 1
        elif (n == 2):
            return 2
        elif (n == 0):
            return 0
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


    def climbStairs3(self, n,m):#if m is not a fix number
        """
        :type n: int
        :rtype: int
        """
        a = np.full(n + 1, 0)
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        elif (n == 2):
            return 2
        else:
            a[0] = 1
            a[1] = 1
            for i in range(2, n + 1):
                for j in range(1,m+1):
                    if(i-j>=0):
                        a[i]+= a[i - j]
        print(a[n])
        return int(a[n])

s=Solution()
s.climbStairs3(6,5)