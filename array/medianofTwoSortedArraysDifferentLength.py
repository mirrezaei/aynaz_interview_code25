import math
# arrays do not have the same length necessarily

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)>len(nums2):
            la=nums1
            sm=nums2
        else:
            la=nums2
            sm=nums1
        l=len(la)
        s=len(sm)

        imin=0
        imax=s
        m=(l+s+1)/2

        while(imin<imax):
            i=(imin+imax)/2
            j=m-i

            #i and j refer to right side
            #i-1 and j-1 refer to left side
            if i<s and sm[i]<la[j-1]:#i too small
                imin=i+1
            elif i>0 and sm[i-1]>la[j]:# i too big
                imax=i-1
            else: # i exact place

                if i==0: maxLeft=la[j-1]
                elif j==0: maxLeft=sm[i-1]
                else: maxLeft=max(la[j-1],sm[i-1])
                if (s+l)%2==1: #sum of the two array is not even
                    return maxLeft

                if i==s: minRight=l[j]
                elif j==l: minRight=s[i]
                else: minRight=min(la[j],sm[i])

                return (maxLeft+minRight)/2











class Solution2(object):
     def assign(self,i,j,m,n,s,l):
         if (i == n):
             sRight = float('inf')
             sLeft = s[i - 1]
         elif (i == 0):
             sLeft = float('-inf')
             sRight = s[i]
         else:
             sLeft = s[i - 1]
             sRight = s[i]
         if (j == 0):
             lLeft = float('-inf')
             lRight = l[j]
         elif (j == m):
             lRight = float('inf')
             lLeft = l[j - 1]
         else:
             lRight = l[j]
             lLeft = l[j - 1]
         return sLeft, lRight, lLeft, sRight

     def findMedianSortedArrays(self, nums1, nums2):
            """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
            # m is the length of larger array, n for smaller array
            if(len(nums1)==0 and len(nums2)==0):
                return None
            elif(len(nums1)==0):
                m=len(nums2)
                if(m%2==0):
                    return np.mean([nums2[m/2],nums2[m/2-1]])
                else:
                    return nums2[m/2]
            elif (len(nums2) == 0):
                m = len(nums1)
                if (m % 2 == 0):
                    return np.mean([nums1[m/2], nums1[m/2 - 1]])
                else:
                    return nums1[m/2]
            else:
                if(len(nums2)>len(nums1)):
                    m = len(nums2)#larger
                    n = len(nums1)#smaller
                    s=nums1
                    l=nums2
                else:
                    n = len(nums2)
                    m = len(nums1)
                    s=nums2
                    l=nums1
                minInd=0
                maxInd=n
                i=(minInd+maxInd)/2
                j=(n+m+1)/2-i

                sLeft,lRight,lLeft,sRight=self.assign(i,j,m,n,s,l)
                while(sLeft>lRight or lLeft>sRight):
                    if(sLeft>lRight ):
                        maxInd = i - 1
                    if(lLeft>sRight):
                        minInd=i+1
                    i = (minInd + maxInd) / 2
                    j = (n + m + 1) / 2 - i
                    sLeft, lRight, lLeft, sRight = self.assign(i, j, m, n,s,l)


                if((m+n)%2==0):
                    median=np.mean([max(sLeft,lLeft),min(sRight,lRight)])
                else:
                    median=max(sLeft,lLeft)




            print(median)
            return median

s=Solution()
nums1 = [1,2]
nums2 = [3]


print(s.findMedianSortedArrays(nums1,nums2))
