#(Here, the distance between two points on a plane is the Euclidean distance.)

#You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
import heapq
class Solution(object):
    def kClosest2(self, points, K):#O(nlog n)
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return sorted(points,key= lambda x: x[0]**2+x[1]**2)[:K]

    def kClosest(self, points, K):#o(n log(k))
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        h = []
        for p in points:
            dis = -p[0] ** 2 - p[1] ** 2
            heapq.heappush(h, (dis, p))
            if (len(h) > K):
                heapq.heappop(h)

        return [p[1] for p in h]


