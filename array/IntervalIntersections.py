#You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
#Return the intersection of these two interval lists.
#A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.
#The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].


# Start traversing the two arrays from begining
#there are two pointers to the intervals to each list
#potential start= compare the starts and find the max
#potential end=compare the ends and find the min
#if the potential start is less than potential end, then this is an appropriate interval
#otherwise move the pointer that has smaller end

class Solution(object):
    def intervalIntersection(self, A, B):# best approach
        i = 0
        j = 0
        out = []
        while (i < len(A) and j < len(B)):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            if (start <= end):
                out.append([start, end])

            if (B[j][1] < A[i][1]):#move the pointer with smaller end
                j += 1
            else:
                i += 1

        return out
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        out = []
        while (i < len(A) and j < len(B)):
            if (A[i][0] < B[j][0]):
                if (B[j][0] <= A[i][1]):  # there is an overlap
                    start = B[j][0]
                    if (A[i][1] < B[j][1]):
                        end = A[i][1]
                        i += 1
                    else:
                        end = B[j][1]
                        j += 1
                    out.append([start, end])
                else:  # no overlap
                    i += 1

            else:
                if (A[i][0] <= B[j][1]):
                    start = A[i][0]
                    if (B[j][1] < A[i][1]):
                        end = B[j][1]
                        j += 1
                    else:
                        end = A[i][1]
                        i += 1
                    out.append([start, end])
                else:
                    j += 1
        return out

#2025s