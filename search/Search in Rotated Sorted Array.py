#You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
#Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#If target is found in the array return its index, otherwise, return -1.

# we need to modify the binary search
# the rotated version of the array only happens at one side of the array
#it means one side is still ascending and one side is not ascending
# so we need to find out which part of the array (right or left) is ascending by comparing the first and last element of that part
#if the right is ascending , there are two options:
#1) target is between right-start and right-end ; so we only search that right part
#2) the elemen is not in the right ; so it is definitely in the left
#we repeat the same process for the left side

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def biSearch(i, j):
            if i <= j:
                m = (i + j) / 2
                if nums[m] == target:
                    return m
                else:
                    right = False
                    left = False
                    if m + 1 < len(nums) and nums[m + 1] <= nums[j]:#right is sorted
                        right = True
                    if m - 1 > -1 and nums[i] <= nums[m - 1]:#left is sorted
                        left = True
                    if right:
                        if target >= nums[m + 1] and target <= nums[j]:#right is sorted and item is in right part
                            return biSearch(m + 1, j)
                        else:
                            return biSearch(i, m - 1)
                    elif left:
                        if target >= nums[i] and target <= nums[m - 1]:#left is sorted and item is in left part
                            return biSearch(i, m - 1)
                        else:
                            return biSearch(m + 1, j)
                    else:
                        return -1
            else:
                return -1

        if len(nums) == 0:
            return -1
        return (biSearch(0, len(nums) - 1))


s=Solution()
nums=[3,4,5,6,1,2]
target=2

#nums=[4,5,6,7,0,1,2]
#target=3

nums=[1]
target=0
print(s.search(nums,target))