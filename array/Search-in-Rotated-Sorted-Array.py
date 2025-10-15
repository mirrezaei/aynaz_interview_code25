 #There is an integer array nums sorted in ascending order (with distinct values).
#Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.


# we need to modify the binary search
# the rotated version of the array only happens at one side of the array
#it means one side is still ascending and one side is not ascending
# so we need to find out which part of the array (right or left) is ascending by comparing the first and last element of that part
#if the right is ascending , there are two options:
#1) target is between middle point and end of array ; so we only search that right part
#2) otherwise: (the element is not in the right) ; so it is definitely in the left
#we repeat the same process for the left side
#if the left is ascending , there are two options:
#1) target is between the start point and middle of array ; so we only search the left part
#2) otherwise: (the element is not in the left) ; so it is definitely in the righ

#it is the binary search with the only difference that in binary search we usually compare with the middle element only. However, in this binary search we need to compare with the left or right element as well

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right
                else:
                    right = mid - 1  # Search left

        return -1




s=Solution()
nums=[3,4,5,6,1,2]
target=2

#nums=[4,5,6,7,0,1,2]
#target=3

nums=[1]
target=0
print(s.search(nums,target))

#2025