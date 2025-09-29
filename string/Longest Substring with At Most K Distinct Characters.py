# Given a string S, find the length of the longest substring T that contains at most k distinct characters.

# the whole idea: we create a dict to keep the last occurrence of our distinct chars
# as we move forward we update the dict
# if the number of distinct chars is m ore than K, then we need to remove chars and update the dict
# meanwhile we should keep track of longest substring, number of distinct chars, and a pointer to start of string

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        if (s == "" or k == 0):
            return 0
        maxLen = 0# longest substring we found so far
        count = 1#number of distinct chars
        curCh = {s[0]: 0}  # the last occcurence of a char
        curLen = 1
        start = 0# the start of substring
        for i in range(1, len(s)):
            if (s[i] in curCh):
                curLen += 1
                curCh[s[i]] = i #the last occcurence of a char
            else:
                count += 1
                curCh[s[i]] = i
                if (count > k):# if number of our distinct chars in the substring is greater than K
                    if (curLen) > maxLen:
                        maxLen = curLen
                    while (len(curCh) > k):# we need to delete from substring so that we can reach to k distinct chars
                        if (curCh[s[start]] == start):#only delete it when you are sure this is the last one, because we may have more from this chars
                            del curCh[s[start]]
                        start += 1
                    curLen = i - start + 1
                    count -= 1
                else:
                    curLen += 1
        if (curLen) > maxLen:
            maxLen = curLen
        return maxLen

#Input: S = "eceba" and k = 3
#Output: 4
#Explanation: T = "eceb"

#Input: S = "WORLD" and k = 4
#Output: 4
#Explanation: T = "WORL" or "ORLD"