#Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

#[0,0] , k=-1  True
#[0,1,0], k=0 False
#[0,0], k=0   True

#the idea of the solution is that if there is a consecutive sequence from i-j that its sum%k==0, then this condition should be true:
# sum[i-1]%k==sum[j]%k. becasue no mater what has been the sum[i-1]%k, the sequence  from i-j should have sum%k==0, therefore sum[i-1]%k should not have changed technically
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if (k == 0):
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))# if there are any two consecutive zeros or not
        sum = 0
        d = {0: -1}
        for i in range(len(nums)):
            sum += nums[i]
            if (sum % k in d):
                if (i - d[sum % k] > 1):#make sure that subarray has at least len of 2
                    return True
            else:
                d[sum % k] = i# we only need to keep the first % that we have seen , not all of them
        return False

nums=[0,1,0]
k=0
nums=[0,0]#,k=-1
so=Solution()
print(so.checkSubarraySum(nums,k))

#2025