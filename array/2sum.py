#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in d.keys():
                j = target - nums[i]
                if (d[j] != i):
                    return ([i, d[j]])
#Updated
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers={}
        for i,num in enumerate(nums):
            if target-nums[i] in numbers :
                return ([i,numbers[target-nums[i]]])
            numbers[num]=i

#2025