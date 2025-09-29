#Given the radius and x-y positions of the center of a circle, write a function randPoint which generates a uniform random point in the circle.

#Note:

#input and output values are in floating-point.
#radius and x-y position of the center of the circle is passed into the class constructor.
#a point on the circumference of the circle is considered to be in the circle.
#randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.

import random, math


class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        lx = self.x_center - self.radius
        ux = self.x_center + self.radius
        ly = self.y_center - self.radius
        uy = self.y_center + self.radius

        while (True):
            r1 = random.uniform(lx, ux)
            r2 = random.uniform(ly, uy)

            if (math.sqrt(pow(r1 - self.x_center, 2) + pow(r2 - self.y_center,2)) < self.radius):
                print([r1, r2])
                return ([r1, r2])

# Your Solution object will be instantiated and called as such:
obj = Solution(1, 0, 0)
param_1 = obj.randPoint()