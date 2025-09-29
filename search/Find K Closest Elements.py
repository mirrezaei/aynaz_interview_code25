#Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
#An integer a is closer to x than an integer b if:
#|a - x| < |b - x|, or
#|a - x| == |b - x| and a < b

class Solution(object):
    def search(self, a, x):
        l = 0
        r = len(a) - 1
        while (l <= r):
            m = (l + r) / 2
            if a[m] == x:
                return m
            elif (x < a[m]):
                r = m - 1
            else:
                l = m + 1
        if(l<len(a) and r>=0):
            return r if  abs(a[r]-x)<=abs(a[l]-x) else  l  #decide too return left ro right
        return l if r<0 else r

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        ind = self.search(arr, x)# find the closest position in the list first
        if ind == len(arr):
            return arr[len(arr)-k :]
        i = ind
        j = ind
        count = 1
        while count < k:
            if i > 0 and j < len(arr) - 1:
                if(abs(arr[i-1]-x)<=abs(arr[j+1]-x)):
                    i -= 1
                    count += 1
                else:
                    j += 1
                    count += 1
            elif i<=0 and j < len(arr) - 1:
                j += 1
                count += 1
            elif j>=len(arr) - 1 and i>0:
                i -= 1
                count += 1
            else:
                break

        return arr[i:j + 1]
arr = [1,2,3,4,5]
#arr = [1,3,4,8,10,20,30]
#arr=[0,1,1,1,2,3,6,7,8,9]
arr=[0,0,1,2,3,3,4,7,7,8]
#arr=[0,0,0,1,3,5,6,7,8,8]


k = 4
x = 2
s=Solution()
print(s.findClosestElements(arr,k,x))


