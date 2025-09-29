#Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

#If there isn't any rectangle, return 0.

#solution 1:
#1-1: using 3 points of a rectangle we can find the fourth point O(n^3). if p1 and p3 are the points in oppiste corner then we have p1+(p3-p1)+(p2-p1)=p4. In order to find p1,p2 and p3; we need to compute permutation , not combination
#1-2: we need to check if the vectors are perpendicular or not

#solution 2:
# the diameters of the rectangular have the same middle point and if we assume the middle point as the center of a circule then the radius is the same for the four corners of the rectangular
# for each pair of points find the middle point and the radius. create a hash based on the radius and center and the points that have the same keys are candidate for rectangulats
import math
import numpy as np

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        area = float('inf')
        d = set()
        for i in range(len(points)):
            d.add(tuple(points[i]))
        for i in range(len(points)):
            for j in range( len(points)): #permutation matters, not combinations. Orders are important
                if(i==j):
                    continue
                for k in range(j + 1, len(points)):
                    if(k==i or k==j):
                        continue
                    aa=points[i][0] + points[k][0] - points[j][0]
                    bb=points[i][1] + points[k][1] - points[j][1]
                    if ((aa, bb) in d and  abs(np.dot((aa-points[i][0],bb-points[i][1]),(aa-points[k][0],bb-points[k][1])))==0):
                        a = math.sqrt(pow(points[j][0] - points[i][0], 2) + pow(points[j][1] - points[i][1], 2)) * math.sqrt(pow(points[j][0] - points[k][0], 2) + pow(points[j][1] - points[k][1], 2))
                        if (a < area):
                            area = a
        print(area)
        return 0 if area == float('inf') else area




inp=[[0,3],[1,2],[3,1],[1,3],[2,1]]
inp=[[0,2],[0,1],[3,3],[1,0],[2,3],[1,2],[1,3]]
inp=[[1,2],[2,1],[1,0],[0,1]]
inp=[[0,1],[1,0],[3,2],[2,3],[0,3],[1,1],[3,3],[0,2]]
inp=[[0,3],[1,2],[3,1],[1,3],[2,1]]
so=Solution()
so.minAreaFreeRect(inp)


