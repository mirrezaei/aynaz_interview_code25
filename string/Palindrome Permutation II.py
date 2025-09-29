#Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.


import collections
from collections import Counter

#the ieda is simple
#1) check if it is possible to have palindrome permutations or not, by counting the number of chars. there should be all even except one odd
#2) try to generate permutations of half of the sring only
#3) we generate strings level by level (string length). And each string has a small dictionary that represnts the number of chars it has used until now
#we keep track of the number of chars in a string until we use half of the number of chars that we have

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if (len(s) == 0):
            return []
        if (len(s) == 1):
            return ([s])
        d = Counter(s)
        count = 0
        oddChar = ""
        for ch in d:
            if (d[ch] % 2 != 0):
                count += 1
                oddChar = ch
                d[ch] = (d[ch] - 1) / 2
                if (count > 1): #if there is a character with odd counting more than 1; there is no palindrome
                    return []
            else:
                d[ch] = d[ch] / 2
        firstDic = {}
        for ch in d:
            firstDic[ch] = 0
        out = [('', firstDic)]# the idea is that for each string we keep a dictionary that shows the number of characters it has used
        cur = []
        i = 0

        while (i < len(s) / 2):#  i refers  to the strings with length i
            curSet = set()
            for elem in out:  # for each string with length i
                curStr = elem[0]
                for k in elem[1]:
                    curDic = dict(elem[1])
                    if (d[k] - curDic[k] > 0):
                        curDic[k] += 1
                        if (curStr + k not in curSet):
                            cur.append((curStr + k, curDic))

            i += 1
            out = list(cur)
            cur = []

        o = []
        for i in range(len(out)):#append the other half of the string
            if (count == 0):
                o.append(out[i][0] + out[i][0][::-1])
            else:
                o.append(out[i][0] + oddChar + out[i][0][::-1])
        return o


s=Solution()
print(s.generatePalindromes("a"))