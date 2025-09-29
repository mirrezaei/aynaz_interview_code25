class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        out = []

        if (nums == []):
            if (lower == upper):
                out.append(str(upper))
            else:
                out.append(str(lower) + "->" + str(upper))
            return out

        last = lower - 1
        for i in range(len(nums)):
            if (nums[i] < lower):
                continue
            elif (nums[i] > upper):
                out.append(str(last + 1) + "->" + str(upper))
                return out
            elif (nums[i] == last + 2):
                out.append(str(last + 1))
                last = nums[i]
            elif (nums[i] > last + 2):
                out.append(str(last + 1) + "->" + str(nums[i] - 1))
                last = nums[i]
            else:
                last = nums[i]
        if (nums[i] < upper):
            if (last == upper - 1):
                out.append(str(upper))
            else:
                out.append(str(nums[i] + 1) + "->" + str(upper))
        return out
