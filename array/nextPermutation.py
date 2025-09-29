#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

#If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

#The replacement must be in-place and use only constant extra memory.

#Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#1,2,3 -> 1,3,2
#3,2,1 -> 1,2,3
#1,1,5 -> 1,5,1
#1,5,8,4,7,6,5,3  -> 1,5,8,5,3,4,6,7


#the idea is that to find the right section of the sequence that has the largest possible permutation and we can make it larger
# for example in the above example the section is "7,6,5,3", so we can't do anything with that. we need to find number "4" to switch that
#we need the number of the left side of the above right section
class Solution(object):
    def reverse(self, ar, i):
        j = len(ar) - 1
        for k in range(i, int((len(ar) - i) / 2 + i)):
            tmp = ar[j]
            ar[j] = ar[k]
            ar[k] = tmp
            j -= 1
        return ar

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if (len(nums) == 1):
            return nums
        j = len(nums) - 1
        i = len(nums) - 1
        while (i > 0):
            if (nums[i] <= nums[i - 1]):#continue as long as digits are increasing
                i -= 1
            else:#nums[i - 1] should be replaced with a larger number
                if (nums[j] > nums[i - 1]):#if nums[j] is large enough
                    tmp = nums[i - 1]
                    nums[i - 1] = nums[j]
                    nums[j] = tmp
                    nums = self.reverse(nums, i)
                    return nums
                else:
                    j -= 1
        nums = self.reverse(nums, 0)#if there is nothing greater than sequence
        return nums

s=Solution()
num=[1,5,8,4,7,6,5,3]
print(s.nextPermutation(num))

#2025

