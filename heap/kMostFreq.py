#Top K Frequent Words
#Given a non-empty list of words, return the k most frequent elements.

#Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
import heapq
import collections

class Solution(object):
    def topKFrequent_leetcode(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        o=heapq.nlargest(k, count.keys(), key=count.get)
        print(o)
        return o

    def topKFrequent3(self, words, k):# with no hash
        h = []
        d = {}
        i = 0
        m = k
        for w in words:
            if (w not in d.keys()):
                d[w] = [-1, None]
            else:
                d[w][0] = d[w][0] - 1
        f = {}
        for w in words:
            if (d[w][0] not in f.keys()):
                f[d[w][0]] = set()
            f[d[w][0]].add(w)

        for k in f.keys():
            if (len(f[k]) > 1):
                f[k] = list(f[k])
                f[k].sort()
        i=0
        o=[]
        for k in range(min(f.keys()),0):
            if k in f.keys():
                for w in f[k]:
                    if (i < m):
                        o.append(w)
                        i=i+1
        print(o)
        return o



    def topKFrequent2(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        h = []
        d = {}
        i = 0
        m=k
        for w in words:
            if (w not in d.keys()):
                d[w] = [-1,None]
            else:
                d[w][0] = d[w][0] - 1
        f={}
        for w in words:
            if(d[w][0] not in f.keys()):
                f[d[w][0]]=set()
            f[d[w][0]].add(w)

        for k in f.keys():
            if(len(f[k])>1):
                f[k]=list(f[k])
                f[k].sort()
        i=0
        for k in range(min(f.keys()),0):
            if k in f.keys():
                for w in f[k]:
                    if (i < m):
                        if (d[w][1] != None):
                            h[d[w][1]] = (d[w][0], w)
                            heapq.heapify(h)
                        else:
                            heapq.heappush(h, (d[w][0], w))
                            i = i + 1
                        for elem in h:
                            po = h.index(elem)
                            d[elem[1]][1] = po


        output = {}
        o = []
        while (len(h) > 0):
            elem = heapq.heappop(h)
            if (elem[0] not in output.keys()):
                output[elem[0]] = []
            output[elem[0]].append(elem[1])
        for ke in output.keys():
            if (len(output[ke]) > 1):
                output[ke].sort()
        for ke in range(min(output.keys()),0):
            if (ke in output.keys()):
                l_out = output[ke]
                for i in range(len(l_out)):
                    o.append(l_out[i])
        print(o)
        return o


    def topKFrequent1(self, words, k):#streaming point of view using minheap
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        h = []
        d = {}
        i = 0
        for w in words:
            if (w not in d.keys()):
                d[w] = [1,None]
            else:
                d[w][0] = d[w][0] + 1
            if (i < k): # minheap is not full
                if(d[w][1]!=None):#it exists already in the heap
                    h[d[w][1]]=(d[w][0],w)
                    heapq.heapify(h)
                else:
                    heapq.heappush(h, (d[w][0], w))
                    i=i+1
                for elem in h:  #the only problem of this algo is that we need to update the index of all the heap members in the dictionary
                    po=h.index(elem)
                    d[elem[1]][1]=po
            else:#minheap is full
                if (d[w][1] != None):#it exists already in the heap
                    h[d[w][1]]= (d[w][0],w)
                    heapq.heapify(h)
                else:
                    elem = heapq.heappop(h)# elem is the min elem in the heap
                    d[elem[1]][1]=None
                    if (elem[0] < d[w][0]):
                        heapq.heappush(h, (d[w][0], w))
                    elif(elem[0] > d[w][0]):
                        heapq.heappush(h, (elem[0], elem[1]))
                    else:
                        if(elem[1]<w):
                            heapq.heappush(h, (elem[0], elem[1]))
                        else:
                            heapq.heappush(h, (d[w][0], w))

                for elem in h:
                    po=h.index(elem)
                    d[elem[1]][1]=po
        output = {}
        o = []
        while (len(h) > 0):
            elem = heapq.heappop(h)
            if (elem[0] not in output.keys()):
                output[elem[0]] = []
            output[elem[0]].append(elem[1])
        for ke in output.keys():
            if (len(output[ke]) > 1):
                output[ke].sort()
        for ke in range(max(output.keys())+1,0,-1):
            if (ke in output.keys()):
                l_out = output[ke]
                for i in range(len(l_out)):
                    o.append(l_out[i])
        print(o)
        return o

words=["i", "love", "leetcode", "i", "love", "coding"]

s=Solution()
s.topKFrequent1(words,1)


