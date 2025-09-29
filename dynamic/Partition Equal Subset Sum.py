#Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#Input: nums = [1,5,11,5]
#Output: true
#Explanation: The array can be partitioned as [1, 5, 5] and [11].


# the idea is to see if we can create sum/2 with the current coins

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

        if (sum % 2 != 0):
            return False
        sum = sum / 2
        print(sum)
        ar = [[False for j in range(len(nums) + 1)] for i in range(sum)]
        # ar[i][j]: we can reach sum i with elements until positions jth in nums
        for i in range(len(ar)):
            for j in range(1, len(ar[0])):
                if i + 1 == nums[j - 1]:
                    ar[i][j] = True
                else:
                    if i - nums[j - 1] >= 0:
                        ar[i][j] = ar[i][j - 1] or ar[i - nums[j - 1]][j - 1]
                    else:
                        ar[i][j] = ar[i][j - 1]

        return ar[sum - 1][len(nums)]

a=[2,1,5,5,9]
a=[28,63,95,30,39,16,36,44,37,100,61,73,32,71,100,2,37,60,23,71,53,70,69,82,97,43,16,33,29,5,97,32,29,78,93,59,37,88,89,79,75,9,74,32,81,12,34,13,16,15,16,40,90,70,17,78,54,81,18,92,75,74,59,18,66,62,55,19,2,67,30,25,64,84,25,76,98,59,74,87,5,93,97,68,20,58,55,73,74,97,49,71,42,26,8,87,99,1,16,79]
s=Solution()
print(s.canPartition(a))