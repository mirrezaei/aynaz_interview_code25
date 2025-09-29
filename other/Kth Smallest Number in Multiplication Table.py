#there is the possibility to solve this solution using a heap but the time complexity is still in order of mn log k; however there is still better appraoches avalable log mn
#we need to do binary search.  at each time we find how many numbers there are in the left side of the middle
#if the left side number is equal to the K, WE DO NOT STOP. because:
#1) the number may not belong to the table, so we need to find the smallest number that has the above criteria. the smallest number definitely is from the table
#2) k=5, number=7 --> we find out 7 has is the 10th number in the table, so we continue binary search and find out there is no number with k=5; however, we had the below situation
# 1,2,4,6,7,7,7,7,7  ---> 7 is 5th number and we need to find the smallest number
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def correct(num):
            count = 0
            upper = min(num, m)

            for i in range(1, upper + 1):
                count += min(n, num // i)
            return count

        hi = m * n
        lo = 1
        while (lo <= hi):
            print(str(lo) + " ," + str(hi))
            mi = (hi + lo) / 2
            count = correct(mi)
            print(count)
            if (count >= k):
                hi = mi - 1
            else:
                lo = mi + 1
        return lo
m=45
n=12
k=471

m=42
n=34
k=401
s=Solution()
print(s.findKthNumber(m,n,k))