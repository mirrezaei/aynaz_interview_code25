#Given two arrays, write a function to compute their intersection.



from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        out = []
        for k in d1:
            if (k in d2):
                m = min(d1[k], d2[k])
                for i in range(m):
                    out.append(k)
        return out

#2025
nums1=[1,4,7,8]
nums2=[4,5,1,3]
s=Solution()
print(s.intersect(nums1,nums2))