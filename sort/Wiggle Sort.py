#Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if (i % 2 == 0):
                if (nums[i] > nums[i + 1]):
                    tmp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = tmp
            else:
                if (nums[i] < nums[i + 1]):
                    tmp = nums[i + 1]
                    nums[i + 1] = nums[i]
                    nums[i] = tmp
