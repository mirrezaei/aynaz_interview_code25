#Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

#You may assume that the intervals were initially sorted according to their start times.

#Example 1:

#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        i = 0

        # Step 1: Add all intervals that come before the new_interval (no overlap)
        while i < len(intervals) and intervals[i][1] < newInterval[0]:#integrate all the intervals that their end point are behind the start point of the new interval
            result.append(intervals[i])
            i += 1
        # at this point we found thge first interval that its end point is after the start of new interval and needs to be merged
        # Step 2: Merge overlapping intervals with the new_interval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:#integrate all the intervals that their start points are behind the end of new interval
            newInterval[0] = min(newInterval[0], intervals[i][0])  # Merge start
            newInterval[1] = max(newInterval[1], intervals[i][1])  # Merge end
            i += 1
        result.append(newInterval)  # Add the merged interval

        # Step 3: Add all intervals that come after the new_interval (no overlap)
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result


class Solution2(object):
    def search(self,a, start):
        l = 0
        r = len(a) - 1
        found = -1
        while (l <= r):
            m = (l + r) / 2
            if (a[m][0] < start):
                found =m
                l = m+1
            else:
                r = m-1
        return found

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        place = self.search(intervals, newInterval[0])

        if(place==-1):#should be added at the beginning
            start = newInterval[0]
            startInd = 0
        else:
            if (newInterval[0] > intervals[place][1]):
                start = newInterval[0]
                startInd=place+1
            elif( newInterval[1]<intervals[place][1]):
                return intervals
            elif(place==len(intervals)-1 or (place<len(intervals)-1 and  newInterval[1]<intervals[place+1][0])) :
                newend=newInterval[1]
                intervals[place][1]=newend
                return intervals
            else:
                start=intervals[place][0]
                startInd=place

        current=startInd
        while(current<len(intervals)):
            if(newInterval[1]>intervals[current][1]):
                del intervals[current]
            elif(newInterval[1]>=intervals[current][0]):
                intervals[current][0]=start
                return intervals
            else:
                newend=newInterval[1]
                intervals.insert(current,[start,newend])
                return intervals

        newend = newInterval[1]
        intervals.insert(current, [start, newend])
        return intervals
s=Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
newInterval=[9,17]
newInterval=[17,20]
#newInterval=[-1,0]


print(s.insert(intervals,newInterval))

#2025






