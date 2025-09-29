#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (len(nums) == 0):
            return None
        maxPrev = nums[0]
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            maxPrev = max(nums[i], maxPrev + nums[i])
            if (maxPrev > maxSoFar):
                maxSoFar = maxPrev
        return maxSoFar

#num[i]: the largest sum of elements that end with element i, or the element[i] itself
# keep track of largest sum

