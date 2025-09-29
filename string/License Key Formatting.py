class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        i = len(S) - 1
        final = ""
        cur = []
        while (i >= 0):
            if (S[i] != "-"):
                if (len(cur) < K):
                    cur.append(S[i])
                else:
                    t = ""
                    for j in range(K - 1, -1, -1):
                        t += cur[j]
                    final = t + final
                    if (i >= 0):
                        final = "-" + final
                    cur = []
                    cur.append(S[i])
            i -= 1
        if (len(cur) > 0):
            t = ""
            for i in range(len(cur) - 1, -1, -1):
                t += cur[i]
            final = t + final
        print(final)
        return final



s="5F3Z-2e-9-w"
k=4
s="2-5g-3-J"
k=2
s="25-3-j"
so=Solution()
so.licenseKeyFormatting(s,k)