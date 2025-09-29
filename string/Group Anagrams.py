
#Given an array of strings, group anagrams together.

class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        out = []
        for s in strs:
            v = [0 for i in range(26)]
            for ch in s:
                v[ord(ch) - 97] += 1
            if (tuple(v) not in d):
                d[tuple(v)] = []
            d[tuple(v)].append(s)
        for key in d:
            temp = []
            for val in d[key]:
                temp.append(val)
            out.append(temp)
        return out

class Solution2(object): #doesn't work
    def rabinKarp(self,s):# it is wrong
        q=11
        d=5
        hash=0
        for i in range(len(s)):
            hash=(d*hash+ord(s[i]))%q

        return hash


    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for str in strs:
            h=self.rabinKarp(str)
            if(h not in d):
                d[h]=[]
            d[h].append(str)
        out=[]
        for k in d:
            tmp=[]
            for elem in d[k]:
                tmp.append(elem)
            out.append(tmp)
        return out

Input= ["eat", "tea", "tan", "ate", "nat", "bat"]
s=Solution2()
print(s.groupAnagrams(Input))
