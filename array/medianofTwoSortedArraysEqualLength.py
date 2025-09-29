from __future__ import division
import math
import numpy as np

#condition is that both arrays should have the same length
class Solution(object):
    def search(self,l1, r1, l2, r2, num1, num2):
        if (r1 - l1 == 1 and r2 - l2 == 1):
            l = num1[l1:r1 + 1] + num2[l2: r2 + 1]
            l.sort()
            return (l[1] + l[2]) / 2

        elif(r1 - l1 == 0 and r2 - l2 == 0):
            return (num1[0] + num2[0]) / 2

        if ((r2 - l2) % 2 == 0):#odd
            m2 = num2[int(l2 + (r2 - l2) / 2)]
        else:
            m2 = np.mean([num2[l2+int(math.ceil((r2 - l2) / 2))] , num2[l2+int(math.floor((r2 - l2) / 2))]])

        if ((r1 - l1) % 2 == 0):
                m1 = num1[int(l1 + (r1 - l1) / 2)]
        else:
                m1 = np.mean([num1[l1+int(math.ceil((r1 - l1) / 2))] , num1[l1+int(math.floor((r1 - l1) / 2))]])


        if (m1 == m2):
            return m1
        elif (m1 < m2):
                if ((r2 - l2) % 2 == 0):#odd
                    r2 = r2 - ((r2 - l2) / 2)
                else:
                    r2 = r2 - math.floor((r2 - l2) / 2)
                if ((r1 - l1) % 2 == 0):#even
                    l1 = l1  + (r1 - l1) / 2
                else:
                    l1 = l1 + math.floor((r1 - l1) / 2)
        else:
                if ((r1 - l1) % 2 == 0):
                    r1 = r1 - ((r1 - l1) / 2)
                else:
                    r1 = r1 - math.floor((r1 - l1) / 2)
                if ((r2 - l2) % 2 == 0):
                    l2 = l2  + (r2 - l2) / 2
                else:
                    l2 = l2 + math.floor((r2 - l2) / 2)

        return self.search(int(l1), int(r1), int(l2), int(r2), num1, num2)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=self.search(0, len(nums1) - 1, 0, len(nums2) - 1, nums1, nums2)
        print(m)
        return m

s=Solution()
#nums1 = [5,8,10,15,16,20]
#nums2 = [12,18,27,30,35,42]

nums1 = [5,8,10,15,16]
nums2 = [12,18,27,30,35]

nums1=[1,2,5]
nums2=[2,3,4]

nums1=[1,2]
nums2=[2,3]

s.findMedianSortedArrays(nums1,nums2)
