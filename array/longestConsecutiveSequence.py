#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#Input: nums = [100,4,200,1,3,2]
#Output: 4



class Solution:
    # @param A : tuple of integers
    # @return an integer

    #O(n log n)
    def longestConsecutive(self, nums): #O(n logn)

        n = len(nums)

        if n == 0:
            return 0

        nums.sort()

        cnt = 1
        maxi = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    cnt += 1
                else:
                    maxi = max(maxi, cnt)
                    cnt = 1

        return max(maxi, cnt)

    # idea: first we addd all the elements in a set, then for each elemnt we check if there is smaller than that or not
    # if there is something smaller, then we move on (ONLY SMALLER)
    # if not we start countinghow many consecutive larger elements exists
    def longestConsecutive(self, A): #BEST APPROACH O(n)
        s=set()
        maxLen=0
        for elem in A:
            s.add(elem)

        for elem in A:
            if(elem-1 not in s):
                len=1
                next=elem+1
                while(next in s):
                    next=next+1
                    len=len+1
                if(len>maxLen):
                    maxLen=len
        print(maxLen)
        return maxLen


    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = 0

        for i in range(len(nums)):
            if nums[i] + 1 not in d:
                cur = nums[i] - 1
                curLen = 1
                while (cur in d):
                    curLen += 1
                    cur -= 1
                maxLen = max(maxLen, curLen)
        return maxLen



    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        d = {}
        if (len(nums) == 0):
            return 0
        for i in range(len(nums)):
            d[nums[i]] = 0
        cur = nums[0]

        def recur(n):
            if (n + 1 in d and d[n + 1] == 0):
                d[n + 1] = recur(n + 1) + 1
                return d[n + 1]
            elif (n + 1 in d):
                return d[n + 1] + 1
            else:
                d[n] = 1
                return d[n]

        for i in range(len(nums)):
            if (d[nums[i]] == 0):
                d[nums[i]] = recur(nums[i])
                if (d[nums[i]] > maxLen):
                    maxLen = d[nums[i]]
        return maxLen

A=[-5]
s=Solution()
s.longestConsecutive(A)

#2025