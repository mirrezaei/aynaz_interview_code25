#You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

#Find out how many ways to assign symbols to make sum of integers equal to target S.

class Solution1(object):

    def findTargetSumWays(self, nums, S):# this solution is based on the idea of recurssion and memoization
        # the idea is to do the recurssion for each element in the nums, from left to right and meanwhile save the pair (s,i) in a hash in case we used it again
        #(s,i): the number of ways we can create the value s using elements in nums array from index i+1 to its end
        #n: len(nums)
        #l: sum of the elements in nums (upper bound)
        #time complexity: if we don't use memoization then time complexity is O(2^n)
        #time complexity: if we use memoriation then we do the recurssion at most l*n (hopefully it is still less than O(2^n))
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def search(s, ind):
            if (ind == len(nums)):
                if (s == 0):
                    return 1
                else:
                    return 0
            else:
                if((s,ind) in d):
                    return d[(s,ind)]
                else:
                    val1=search(s - nums[ind], ind + 1)
                    val2=search(s + nums[ind], ind + 1)
                    d[(s,ind)] = val1+val2


            return d[(s,ind)]
        d={}
        val = search(S,0)
        print(val)
        return val

class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        up=0
        for i in range(len(nums)):
            up+=nums[i]
        a=[float('inf') for i in range(2*len(nums)+1)]
        a[0]=1
        a[-1]=1
        for



nums=[1,1,1,1,1]
S=3
s=Solution()
s.findTargetSumWays(nums,S)