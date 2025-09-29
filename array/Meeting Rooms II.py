#Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.


import heapq
class Solution(object):# O(n log n)
    #sort only beginning and add the end time in a heap
    #if the start of the next time is greater than the min of the heap, pop the heap and insert the new end
    # if the start of the next time is less than the min of the heap, inster the new end end to the heap. it means we need one more room
    #len of heapq at each moment shows the maximum number of rooms we need so far (although the reamin end times in the queue may not be the representative of really rooms needed simultaneously)
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if(len(intervals)==0):
            return 0
        h=[]
        inter=sorted(intervals,key= lambda x:x[0])
        h=[inter[0][1]]
        for i in range(1,len(inter)):
            if(inter[i][0]>=h[0]):
                heapq.heappop(h)
            heapq.heappush(h,inter[i][1])
        return len(h)


class Solution(object):# sort all times including beginning and end times
    def minMeetingRooms(self, intervals):# O(2n log(2n))
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        inter = []
        for i in range(len(intervals)):
            inter.append([intervals[i][0], 'b'])
            inter.append([intervals[i][1], 'a'])
        inter = sorted(inter, key=lambda x: (x[0], x[1]))# if two  number have the same time, first the ending and then the beginning should be sorted
        print(inter)
        maxNow = 0
        cur = 0
        for i in range(0, len(inter)):
            if (inter[i][1] == 'b'):
                cur += 1
                if (maxNow < cur):
                    maxNow = cur
            else:
                cur -= 1
        return maxNow


class Solution(object):# o(n) but space is o(max time)
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if (len(intervals) == 0):
            return 0
        ma = 0

        for i in range(len(intervals)):
            if (intervals[i][0] > ma):
                ma = intervals[i][0]
            if (intervals[i][1] > ma):
                ma = intervals[i][1]
        inp = [0 for i in range(ma + 1)]
        for i in range(len(intervals)):
            inp[intervals[i][0]] += 1
            inp[intervals[i][1]] -= 1
        cur = 0
        ma = 0
        for i in range(len(inp)):
            cur += inp[i]
            if (cur > ma):
                ma = cur

        return ma

#2025
