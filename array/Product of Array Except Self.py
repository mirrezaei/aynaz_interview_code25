#Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

#Note: Please solve it without division and in O(n).

#Follow up:
#Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out=[1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            out[i]=out[i-1]*nums[i-1]
        mul=1
        for i in range(len(nums)-2,-1,-1):
            mul=mul*nums[i+1]
            out[i]=out[i]*mul
        return out

#2025