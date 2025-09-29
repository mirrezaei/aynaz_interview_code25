#Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

#Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

#we need to check two conditions
#1) the area of the entire rectangle should be exactly the same as the total sum of the smaller rectangles'area (find the lower left corner and the upper right corner in order to find the entire rectangle area)
#2) all the corners of the smaller rectangles should be repeated more than once; except the corners matching the entire rectangle's corner
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        corner=set()
        a,b,c,d,area=float('inf'),float('inf'),float('-inf'),float('-inf'),0
        for x1,y1,x2,y2 in rectangles:
            if x1<=a and y1<=b: a=x1; b=y1
            if x2>=c and y2>=d: c=x2; d=y2
            area+=(x2-x1)*(y2-y1)
            corner^={(x1,y1),(x2,y1),(x1,y2),(x2,y2)}
        if(area==(c-a)*(d-b) and corner=={(a,b),(c,b),(a,d),(c,d)}):
            return True
        else:
            return False


rectangles =[[0,0,1,1],[0,1,3,2],[1,0,2,2]]
#rectangles = [[1, 1, 3, 3],[3, 1, 4, 2],[3, 2, 4, 4],[1, 3, 2, 4], [2, 3, 3, 4]]
s=Solution()
s.isRectangleCover(rectangles)