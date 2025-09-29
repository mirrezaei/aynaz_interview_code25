#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#If target is not found in the array, return [-1, -1].

def searchRange(nums, target):  #BEST for left search
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def binary(ar, t):
        # if t exists: return the left most index
        # if t doesn't exist return the index that we should insert it
        l = 0
        r = len(ar)
        while (l < r):
            m = (l + r) / 2
            if (t <= ar[m]):
                r = m
            else:
                l = m + 1
        return l

    left = binary(nums, target)
    right = binary(nums, target + 1)
    print(left)
    print(right)
    return (left, right - 1) if target in nums[left:left + 1] else (-1, -1)


class Solution2(object):#
    #one time we find the most right match
    #one time we find the most left  match
    def binary(self,i,j,n,t,right):
        found=-1
        while(i<=j):
            m = (i + j)/2
            if(n[m]==t):
                found=m
                if(right==True):
                    i=m+1
                else:
                    j=m-1
            elif(n[m]>t):
                j=m-1
            else:
                i=m+1
        return found


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        right=self.binary(0,len(nums)-1,nums,target,True)
        if (right != -1):
            left = self.binary(0, len(nums) - 1, nums, target, False)
        else:
            left = -1
        return(left,right)





nums = [5,7,7,8,8,8,10]
target = 8
#target=6
#s1=Solution1()
#print(s1.searchRange(nums,target))
s2=Solution2()
print(s2.searchRange(nums,target))

#2025