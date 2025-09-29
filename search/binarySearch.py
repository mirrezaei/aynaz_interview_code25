
a=[1,2,2,4,4,4,4,4,5,5]
a=[1,2,2,3,3,3,3,3,4,5]
#a=[1,2,3,4]
a=[3,6,8,8,12]

def searchRange( nums, target):# for left searcch

        #Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
        #If target is not found in the array, return [-1, -1].
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary(ar, t):
            #if t exists: return the left most index
            #if t doesn't exist return the index that we should insert it (the first bigger number)
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


def binarySearch(a,x):# for binary search
    l=0
    r=len(a)-1
    while(l<=r):# =<
        m=(l+r)/2
        if(a[m]==x):
            return m
        elif(x<a[m]):
            r=m-1
        else:
            l=m+1

    return -1



#print(binarySearch(a,2))
#print(searchRange(a,1))
times=[0, 5, 10, 15, 20, 25, 30]

def binarySearch_exacxt_OR_smaller( l, r, t):#do the binary search, return the exact match , in case it doesn't exist return the first smaller value

        while (l < r):
            m = (l + r) / 2
            print(m)
            if times[m] == t:
                return m
            elif t < times[m]:
                r = m
            else:
                l = m + 1
        return l-1


