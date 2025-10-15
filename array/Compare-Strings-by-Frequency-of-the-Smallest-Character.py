#Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.
#You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.
#Return an integer array answer, where each answer[i] is the answer to the ith query.


from collections import Counter
import bisect
class Solution(object):

    def binary(self,wo,t):
        l=0
        r=len(wo)
        while(l<r):
            m=(l+r)//2
            if wo[m]>=t:
                r=m
            else:
                l=m+1
        return l


    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        wo = []
        for w in words:
            wo.append(Counter(w)[min(w)])
        wo.sort()

        for q in queries:
            n = Counter(q)[min(q)]
            #count =len(wo)-bisect.bisect(wo,n)
            count =len(wo)-self.binary(wo,n+1)#point is that we are looking for n+1, so in binary search if there are duplicates of n+1 we should find the left most index of that
            ans.append(count)
        return ans


so=Solution()
queries = ["bbb","cc"]
words = ["a","aa","ccc","bbb","aaa","aaaa"]
print(so.numSmallerByFrequency(queries,words))

#2025