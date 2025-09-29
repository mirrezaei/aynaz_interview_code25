
#From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).
#Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.
import numpy as np
import sys

#m[j][i]:  the position of first occurence of char target[i] after position j in source
class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        m=[[-1]*26 for i in range(len(source))]#len(source)*26
        for i in range(len(source)):#m[i][c]: the nearest char c=source[j] from index i  is at position j of source:  j>=i
            for j in range(i,len(source)):
                if(m[i][ord(source[j])-ord('a')]==-1):
                    m[i][ord(source[j])-ord('a')]=j

        i=0#target
        nu=0
        j=0#source index
        while(i<len(target)):
            if(m[0][ord(target[i])-ord('a')]==-1):#char target[i] doesn't exist in source
                return -1
            if(m[j][ord(target[i])-ord('a')]==-1):#if target[i] doesn't exist right side of index j, it means we need a new subsequence which starts from previous of index j
                nu+=1
                j=0

            ind=m[j][ord(target[i])-ord('a')]#update the start of the window

            j=ind+1
            if(j==len(source)):#if the start is at end of source, reset it to 0 again
                nu+=1
                j=0
            i+=1
        if(j!=0):
            nu+=1
        print(nu)
        return nu







so=Solution()
#s="abca"
#t="abcbc"

#s="abc"
#t="acdbc"

s="xyz"
t="xzyxz"
so.shortestWay(s,t)