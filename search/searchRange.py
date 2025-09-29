
class Solution2(object):# this approach is much better than the other obe
    #one time we find the most right match
    #one time we find the most left  match
    def binary(self,i,j,n,t,right): #if there is an element in the array it can find the left most index or the right most index in the array
        #if the element doesn't exist it cannot find its left existant element or right existant element
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


a=[1,2,2,3,3,3,3,3,4,5]
#a=[1,2,3,4]
a=[3,6,8,8,12]

def searchRange( nums, target):# this approach only finds left index
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary(ar, t):
            #if t exists: return the left most index
            #if t doesn't exist return the index that we should insert it
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

print(searchRange(a,1))
