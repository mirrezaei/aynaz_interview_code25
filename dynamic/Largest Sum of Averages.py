#We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

#Note that our partition must use every number in A, and that scores are not necessarily integers.

class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        su = [0 for i in range(len(A))]

        su[0] = A[0]
        for i in range(1, len(A)):
            su[i] = su[i - 1] + A[i]
        av = su[:]# av[j] refers to the sum of avgerages splits until index j
        for i in range(1, len(A)):
            av[i] = float(av[i]) / float(i + 1)# av[j] refers to the sum of avgerages splits until index j using zero split

        for i in range(1, K ):# the maximum number of times we can split the array
            cur = av[:]# av refers to the sum of avgerages using k-1 split
            for j in range(i, len(A)):
                for l in range(j):#create a new group at this position , new group is in fact (l+1:j)
                    cur[j] = max(cur[j], av[l] + (float(su[j] - su[l]) / (j - l)))
            av=cur # cur refers to the sum of avgerages using k split
        return av[-1]

A=[9,1,2,3,9]
K=3
so=Solution()
print(so.largestSumOfAverages(A,K))
#the idea is to do several iterations over the array A, and at each iteration add one new group to the array
#at the end of  iteration i, av[j] reffers to the largest sum of the averages using  i groups by conidering elements A[0]:A[j]
#repeat this iteration K times and av[-1] is the final result

#Intuition   max(cur[j], av[l] + (float(su[j] - su[l]) / (j - l)))
#av[l] + (float(su[j] - su[l]) / (j - l)): break at position l, create a new group (l+1,j)