#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Determine if you are able to reach the last index.


# the idea is that if we want to reach the last element of the array we have to be able to reach to previous elements as well.
# We traverse the array from left to right, and we shoould be able to meet each element, if we couldn't then we can reach the last element

class Solution(object):
    def canJump(self, nums):# time O(n), space: O(1)   BEST APPROACH
        maxJump = nums[0]
        for i in range(1, len(nums)):
            if i > maxJump:
                return False
            maxJump = max(maxJump, nums[i] + i)

        return True

    def canJump2(self, nums):#O(n^2)  time limit problem, O(n) space
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = [False for i in range(len(nums))]
        s[0] = True
        for i in range(len(nums)):
            if (s[i] == True):
                for j in range(1,nums[i]+1):
                    if (j + i < len(nums)):
                        s[j + i] = True
        print(s)
        return True if s[-1] else False

    def canJump2(self, nums):# time O(n), space: O(n)
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = [False for i in range(len(nums))]
        s[0] = True
        maxJump = nums[0]
        for i in range(1, len(nums)):
            if (i <= maxJump):
                s[i] = True
            else:
                return False
            maxJump = max(maxJump, nums[i] + i)

        print(s)
        return True if s[-1] else False




s=Solution()
nums=[2,3,1,1,4]
nums=[10,1,1]
#nums=[3,2,1,0,4]
#nums=[2,0]
#nums=[0,2,3]
print(s.canJump(nums))


#2025s