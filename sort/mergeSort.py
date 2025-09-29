class Solution(object):
    def merge(self,l, r, m):
        i, j = 0, 0
        while (i < len(l) or j < len(r)):
            if (i >= len(l)):
                while (j < len(r)):
                    m[i + j] = r[j]
                    j += 1
            elif (j >= len(r)):
                while (i < len(l)):
                    m[i + j] = l[i]
                    i += 1
            else:
                if (l[i] > r[j]):
                    m[i + j] = r[j]
                    j += 1
                else:
                    m[i + j] = l[i]
                    i += 1
        return m

    def mergeSort(self, m):
        if (len(m) == 1):
            return m
        else:
            l = self.mergeSort(m[:len(m) / 2])
            r = self.mergeSort(m[len(m) / 2:])
            return self.merge(l, r, m)



so=Solution()
inp=[6,3,4,10,1,5,2,8]
#inp=[4,1]
#inp=[4]
print(so.mergeSort(inp))