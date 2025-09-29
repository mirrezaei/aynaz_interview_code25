#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#dictionary time O(n), space:O(n)
class Solution(object): #time O(n), space:O(1)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in range(len(nums)):
            a ^= nums[i]

        return a

nums=[1,2,1,2,3]
s=Solution()
print(s.singleNumber(nums))

#2025