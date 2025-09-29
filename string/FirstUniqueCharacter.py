#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

#s = "leetcode"
#return 0.

#s = "loveleetcode",
#return 2.
import sys
import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i,c in enumerate(s):
            if(c not  in d.keys()):
                d[c]=[1,i]
            else:
                d[c][0]+=1
        min=sys.maxint
        find=False
        for k in d.keys():
            if(d[k][0] ==1):
                find=True
                if(d[k][1] <min):
                    min=d[k][1]
        if(find==True):
            return min
        else:
            return -1

    def firstUniqChar2(self, s):
        d=collections.Counter(s)
        for i,c in enumerate(s):
            if(d[c]==1):
                return i
        return -1



