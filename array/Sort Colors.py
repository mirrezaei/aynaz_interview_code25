#Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue

#solution: three pointers
#pt0: right index of last 0
#pt2: left index of last 2
#cur: cur pointer (we try to find the right index of 1)

#the idea is that push all the 2s  to the right of pt0
# and all the 0s to the left side of pt0, and then 1s remain between pt0 and pt2


#idea: we start processing the array from left to right by cur pointer:
#:1) if we see 0 by pointer, we change the element with the element at pt0 (elemnt here at pt0 should definitely be 1 or 0), increase both cur and pt0.
#     Point: there is no 2 left side of cur
#2)  if we see 1 by pointer, just pass it and increase the cur
#3) if we see 2, we change the element with the element at pt2 (which could be 0,1 or 2). we only decrease pt2. we cannot increase cur, because we mah have 2 at cur after replacement
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pt0=0
        pt2=len(nums)-1
        cur=0
        while(cur<=pt2):
            if(nums[cur]==0):# if current elem is 0, replace its poistion with pt0 elem, increase pt0 and increase cur
                tmp=nums[pt0]
                nums[pt0]=0
                nums[cur]=tmp
                pt0+=1
                #cur=max(cur,pt0)
                cur+=1
            elif(nums[cur]==2):#if current elem is 2, do not increase cur. jsut replace its position with the pt2 and decrease pt2
                tmp = nums[pt2]
                nums[pt2] = 2
                nums[cur]=tmp
                pt2 -= 1
            else:#current elem is 1
                cur+=1
        return nums


inp=[2,0,2,1,1,0]
inp=[2,2,2,2]
#inp=[2,2,0,0,1,1,0,2,2]
#inp=[2,0,1]
s=Solution()
print(s.sortColors(inp))

#2025