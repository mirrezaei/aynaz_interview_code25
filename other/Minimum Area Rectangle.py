#Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

#If there isn't any rectangle, return 0.

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        d = set()
        for i in range(len(points)):
            d.add(tuple(points[i]))
        area = float('inf')
        for i in range(len(points)):

            for j in range(i + 1, len(points)):
                if (points[i][0] != points[j][0] and points[i][1] != points[j][1] and (
                points[i][0], points[j][1]) in d and (points[j][0], points[i][1]) in d):
                    a = abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1])
                    if (a < area):
                        area = a
        return 0 if area == float('inf') else area






