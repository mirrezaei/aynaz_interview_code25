#Given a collection of intervals, merge all overlapping intervals.


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        s = sorted(intervals, key=lambda x: x[0])
        if (len(s) == 0):
            return []
        elif (len(s) == 1):
            return s
        else:
            beg = s[0][0]
            end = s[0][1]
            for i in range(1, len(s)):
                if (s[i][0] <= end):  # we can mergeL the current start is smller than prevois end, so we can merge
                    if (s[i][1] > end):#if the current end is larger than previous end, create a new end
                        end = s[i][1]
                else:#no merge, add the interval
                    out.append([beg, end])
                    beg = s[i][0]
                    end = s[i][1]
        out.append([beg, end])
        return out



intervals= [[1,3],[2,6],[8,10],[15,18]]
s=Solution()
s.merge(intervals)

#2025

