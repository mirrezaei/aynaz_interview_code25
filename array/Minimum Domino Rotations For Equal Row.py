#Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
#If it cannot be done, return -1.

#idea: overall there are four possible ways to cover this rotation:
# all chars in A are rotated to A[0]
# all chars in A are rotated to B[0]
# all chars in B are rotated to B[0]
# all chars in B are rotated to A[0]

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        a = [A[0], 0]# all chars in A are rotated to A[0]
        aa = [B[0], 1]# all chars in A are rotated to B[0]
        b = [B[0], 0]# all chars in B are rotated to B[0]
        bb = [A[0], 1]# all chars in B are rotated to A[0]
        for i in range(1, len(A)):
            if (a[1] != float('inf')):
                if (A[i] == a[0]):
                    a = a
                elif (B[i] == a[0]):
                    a[1] += 1
                else:
                    a[1] = float('inf')
            if (aa[1] != float('inf')):
                if (A[i] == aa[0]):
                    aa = aa
                elif (B[i] == aa[0]):
                    aa[1] += 1
                else:
                    aa[1] = float('inf')
            if (b[1] != float('inf')):
                if (B[i] == b[0]):
                    b = b
                elif (A[i] == b[0]):
                    b[1] += 1
                else:
                    b[1] = float('inf')
            if (bb[1] != float('inf')):
                if (B[i] == bb[0]):
                    bb = bb
                elif (A[i] == bb[0]):
                    bb[1] += 1
                else:
                    bb[1] = float('inf')
        dd=min(a[1], b[1], aa[1], bb[1])
        return -1 if dd==float('inf') else dd



so=Solution()
A = [3,5,1,2,3]
B = [3,6,3,3,4]
print(so.minDominoRotations(A,B))