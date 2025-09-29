#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxLeft = 0
        maxRight = 0
        maxWater = 0
        while (i < j):
            if (height[i] < height[j]):
                if (height[i] > maxLeft):
                    maxLeft = height[i]
                    water = height[i] * (j - i)
                    if maxWater < water:
                        maxWater = water
                i += 1
            else:
                if (height[j] > maxRight):
                    maxRight = height[j]
                    water = height[j] * (j - i)
                    if maxWater < water:
                        maxWater = water
                j -= 1
        return maxWater

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxWater = 0
        while (i < j):
            if (height[i] < height[j]):
                water = height[i] * (j - i)
                i += 1
            else:
                water = height[j] * (j - i)
                j -= 1
            if maxWater < water:
                maxWater = water
        return maxWater





s=Solution()
inp=[1,8,6,2,5,4,8,3,7]
print(s.trap3(inp))

