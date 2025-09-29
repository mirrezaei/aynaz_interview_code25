#Given a string, sort it in decreasing order based on the frequency of characters.

from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=Counter(s)
        out=""
        so=sorted(d.iteritems(),key=lambda x:x[1],reverse=True)
        for i in range(len(so)):
            for j in range(so[i][1]):
                out += so[i][0]
        print(out)
        return out