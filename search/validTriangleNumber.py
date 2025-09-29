#Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.


class Solution(object):
    def triangleNumber(self, nums):# time complexity O(n^3)
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] > nums[k]):
                        count += 1
                    else:
                        break
        print(count)
        return count

    def triangleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binarySearch(left, right, nu):# replace this by an organized binary search
            m = (left + right) / 2
            if (left - right == 0):
                if (nums[left] < nu):
                    return left
                else:
                    return left - 1
            elif (right - left == 1):
                if (nums[right] < nu):
                    return right
                elif (nums[right] >= nu and nums[left] < nu):
                    return left
                else:
                    return left - 1
            else:
                if (nu > nums[m]):
                    ind = binarySearch(m + 1, right, nu)
                else:
                    ind = binarySearch(left, m - 1, nu)
            return ind

        count = 0
        nums.sort()
        while (len(nums) > 0):
            if (nums[0] == 0):
                del nums[0]
            else:
                break
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 1):
                k = binarySearch(j + 1, len(nums) - 1, nums[i] + nums[j])
                count = count + k - j
        print(count)
        return count

s=Solution()
s.triangleNumber2([82,15,23,82,67,0,3,92,11])