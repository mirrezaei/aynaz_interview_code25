#Given a pattern and a string str, find if str follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.


#for each char in pattern, we consider all possible substrnigs in str
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        def search(i, j, d, prev,vis):
            if (i == len(pattern) and j == len(str)):
                    return True
            elif (i == len(pattern) and j < len(str)):
                return False
            elif (i < len(pattern) and j == len(str)):
                return False
            else:
                if (pattern[i] in d): #if we already assigned a string to the current char in pattern
                    curPt = d[pattern[i]]
                    k = 0
                    while (k < len(curPt)):
                        if (j+k>=len(str) or curPt[k] != str[j + k]):
                            return False
                        k += 1
                    j += k
                    if (search(i + 1, j , d, j ,vis) == True):
                        return True
                else:#if we don't have any assigned str for the current char in pattern
                    cur = str[prev:j + 1]
                    if(cur not in vis): #there is one-to-one bijection
                        vis.add(cur)
                        d[pattern[i]] = cur
                        if (search(i + 1, j + 1, d, j + 1,vis) == True):#new assignment to the current char in pattern
                            return True
                        del d[pattern[i]]
                        vis.remove(cur)

                    if (search(i, j + 1, d, prev,vis) == True):#no assignment to the current char in pattern
                        return True
            return False

        i = 0#pointer to pattern
        j = 0#pointer to str
        prev = 0#the first char in str which has not been assigned to any char in pattern
        d = {}#key: chars in pattern, value: corresponding assignment from str
        vis=set()# the set of strings from str that have been assigned to chars from patterns
        return search(i, j, d, prev,vis)

s=Solution()
pattern="abab"
str="redblueredblue"

#pattern = "aaaa"
#str = "asdasdasdasd"

#pattern = "aabb"
#str = "xyzabcxzyabc"

#pattern = "ab"
#str="aa"

pattern="abba"
str="dogcatcatdog"
print(s.wordPatternMatch(pattern,str))