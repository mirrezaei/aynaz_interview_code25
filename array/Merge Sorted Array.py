#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

#Note:

#The number of elements initialized in nums1 and nums2 are m and n respectively.
#You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = len(nums1) - 1  # refers to the sorted array
        i = n - 1  # refers to the nums2
        k = m - 1  # referes to the nums1

        while (i >= 0 or k >= 0):
            if (i < 0):
                nums1[j] = nums1[k]
                k -= 1
            elif (k < 0):
                nums1[j] = nums2[i]
                i -= 1
            else:
                if (nums1[k] > nums2[i]):
                    nums1[j] = nums1[k]
                    k -= 1
                else:
                    nums1[j] = nums2[i]
                    i -= 1
            j -= 1
        print(nums1)
#2025