import numpy as np
class Solution(object):
    def area(self, height, f, l):
        w = l - f - 1
        h = min(height[f], height[l])
        a = w * h
        for j in range(f + 1, l):
            a -= min(height[j], h)
        return a

    def trap(self, height):# this solution doesn't work. It is wrong. it only finds the area between two peaks
        """
        :type height: List[int]
        :rtype: int
        """
        if (len(height) == 0):
            return 0
        up = False
        f = 0
        l = 0
        total = 0
        i = 0
        while i < len(height) - 1:
            if ((height[i] > height[i + 1] and up == True)):
                l = i
                up = False
                total += self.area(height, f, l)
                f = i
            if (height[i] <= height[i + 1] and up == False):
                up = True
            i += 1
        if (up == True):
            l = i
            total += self.area(height, f, l)
        return total

    def trap2(self, height):# the problem is much space that it takes O(n)
        """
        :type height: List[int]
        :rtype: int
        """
        if (len(height) == 0):
            return 0
        maxLeft = np.zeros(len(height))
        maxRight = np.zeros(len(height))
        maxRight[-1] = height[-1]
        maxLeft[0] = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i])
        res = 0
        for i in range(len(height)):
            res += min(maxLeft[i], maxRight[i]) - height[i]
        return int(res)

    def trap3(self,height):#this approach requires space O(1)
        #the point is that WE ALWAYS MOVE THE SMALLER POINTERS FROM I OR J.
        # for example, when we update maxLeft we are pretty sure it is smaller than maxRight, because we know that i<j. so at least j is larger than maxLeft
        maxLeft=0
        maxRight=0
        res=0
        i=0
        j=len(height)-1
        while(i<j):
            if(height[i]<height[j]):
                if(height[i]>maxLeft):
                    maxLeft=height[i]
                else:
                    res+=maxLeft-height[i]# we don't need the maxRight, because we are pretty sure that maxLeft is smaller than maxRight. Otherwise, we have to move the j to the left until we reach an element wgich is greater than Leftmax
                i+=1
            else:
                if(height[j]>maxRight):
                    maxRight=height[j]
                else:
                    res+=maxRight-height[j]
                j-=1
        return res

s=Solution()
inp=[1,8,6,2,5,4,8,3,7]
print(s.trap3(inp))










