#Given an integer array, find three numbers whose product is maximum and output the maximum product.
#the length of the input is 3


import numpy as np
import sys

class Solution(object):
    def maximumProduct1(self, nums):
        """
        :type nums: List[int]# if the list includes positive numbers
        :rtype: int
        """
        m = np.zeros((2, 3),dtype=np.int32)

        m[0, 0] = max(nums[0:3])
        m[0, 1] = max(nums[0] * nums[1], nums[1] * nums[2], nums[0] * nums[2])
        m[0, 2] = nums[0] * nums[1] * nums[2]

        if (len(nums) > 3):
            for i in range(3, len(nums)):
                m[1, 0] = max(m[0, 0], nums[i])
                m[1, 1] = max(m[0, 0] * nums[i], m[0, 1])
                m[1, 2] = max(m[0, 1] * nums[i], m[0, 2])
                m[0, 0] = m[1, 0]
                m[0, 1] = m[1, 1]
                m[0, 2] = m[1, 2]

        else:
            m[1, 0] = m[0, 0]
            m[1, 1] = m[0, 1]
            m[1, 2] = m[0, 2]
        print(m[1, 2])
        return (m[1, 2])

    def maximumProduct2(self, nums):# if the list includes positive and negative  integers between [-1000,1000]
        #assume a is the sorted array of nums
        # if it includes only positive: return a(n) * a(n-1) * a(n-2)
        # if it includes only negative: retrun a(1) * a(2) * a(n)
        # if both: return a(1) * a(2) * a(n)
        #overal: MAX(a(1) * a(2) * a(n),a(n) * a(n-1) * a(n-2))
        min1=sys.maxint
        min2=sys.maxint
        max1=-sys.maxint
        max2=-sys.maxint
        max3=-sys.maxint

        for i in range(len(nums)):
            if(nums[i]<min1):
                min2=min1
                min1=nums[i]
            elif(nums[i]<min2):
                min2=nums[i]
            if(nums[i]>max1):
                max3=max2
                max2=max1
                max1=nums[i]
            elif(nums[i]>max2):
                max3=max2
                max2=nums[i]
            elif(nums[i]>max3):
                max3=nums[i]

        p=max(max3*max2*max1,max1*min1*min2)
        print(p)
        return p



#a=[-6,3,4,1,7,-8]
a=[-1,-2,-3]
#a=[-1,-2,1,2,3]
#a=[4,2,5,5,6,0]
a=[722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786]
s=Solution()
s.maximumProduct2(a)