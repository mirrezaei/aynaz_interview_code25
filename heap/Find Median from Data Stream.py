import heapq
# the idea is two keep two heaps, one max heap for the lower half and one min heap for the upper half. Then try to grow these two heapa balanced

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h_max = []#lower half
        self.h_min = []#upper half
        self.med = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if (num > self.med):# first check to see if the current num should be add to the upper half or lower half
            if (len(self.h_max) < len(self.h_min)):# if the upper half is already unbalanced
                elem = heapq.heappop(self.h_min)
                heapq.heappush(self.h_max, -elem)
            heapq.heappush(self.h_min, num)
        else:
            if (len(self.h_max) > len(self.h_min)):
                elem = heapq.heappop(self.h_max)
                heapq.heappush(self.h_min, -elem)
            heapq.heappush(self.h_max, -num)


        if (len(self.h_max) == len(self.h_min)):# find the midean depending on the length of heaps
            self.med = float(-(self.h_max[0]) + self.h_min[0]) / 2
        elif (len(self.h_max) > len(self.h_min)):
            self.med = -self.h_max[0]
        else:
            self.med = self.h_min[0]

    def findMedian(self):
        """
        :rtype: float
        """
        return self.med

s=MedianFinder()
s.addNum(1)
print(s.findMedian())
s.addNum(2)
print(s.findMedian())
s.addNum(3)
print(s.findMedian())