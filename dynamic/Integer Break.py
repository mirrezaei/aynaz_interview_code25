#Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

class Solution(object): # if n>4 ->   2*(n-2)=2n-4>0
                                #     3*(n-3)=3n-9
    def integerBreak2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 2):
            return 1
        elif (n == 3):
            return 2
        else:
            p = 1
            while (n > 4):
                n -= 3
                p *= 3
            p *= n
            return p

    def integerBreak(self, n):# a[i]=max[for k<i: max(a[i-k],i-k) * max(k,a[k])]
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return 1
        a = [0 for i in range(n)]
        a[0] = 1
        a[1] = 1
        for i in range(2, n):
            for j in range(0, i):
                a[i]=max(a[i],max(j+1,a[j])*max(i-j,a[i-j-1]))
        print(a)
        return a[-1]

s=Solution()
print(s.integerBreak(10))
#a[i]: is the maximum product for number i
# the idea is to break the i at some point between 0 to i-1, like j; then we need to find the max product of left times max product of right
#left: max(j+1, a[j])
#right: max(i-j,a[i-j-1])
#prod:left*right