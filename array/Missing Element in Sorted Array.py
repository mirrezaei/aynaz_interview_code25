#Given an integer array nums which are sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.


# the idea is to find the element in the array that has seen k missing elements until the left side of its position, --> do this using a binary search
# when we find that element, then we can find the missing number
#number of missing elements until position i:  a[i]-a[0]-i


class Solution(object):
    def search(self, a, k):
        l = 0
        r = len(a) - 1
        found = -1
        while (l <= r):
            m = (l + r) / 2
            if k == a[m] - a[0] - m:# if it has exactly the same numer of missing return that! perfect
                found = m
                return m
            elif k < a[m] - a[0] - m:# just save it in case we didin't find exactly the same number of missing
                found=m
                r = m - 1
            else:
                l = m + 1
        if found==-1 and k>a[-1]-a[0]-len(a)+1:
            found=len(a)
        return found

    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ind = self.search(nums, k)
        print(ind)
        #num[ind-1]+k-missing at index ind-1
        return nums[ind - 1] + k - (nums[ind - 1] - nums[0] - ind + 1)


A = [4,7,9,10]
K = 1

#A=[1,2,4]
#K=3
s=Solution()
print(s.missingElement(A,K))

#2025