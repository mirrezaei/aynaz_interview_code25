class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=2
        if (s == ""):
            return 0
        maxLen = 0
        count = 1
        curCh = {s[0]: 0}#current distinct chars in our substring
        curLen = 1
        start = 0
        for i in range(1, len(s)):
            if (s[i] in curCh):
                curLen += 1
                curCh[s[i]] = i
            else:
                count += 1
                curCh[s[i]] = i
                if (count > k):
                    if (curLen) > maxLen:
                        maxLen = curLen
                    while (len(curCh) > k):
                        if (curCh[s[start]] == start):
                            del curCh[s[start]]
                        start += 1
                    curLen = i - start + 1
                    count -= 1
                else:
                    curLen += 1
        if (curLen) > maxLen:
            maxLen = curLen
        return maxLen






s=Solution()
inp="eceba"
#inp="ccaabbb"
print(s.lengthOfLongestSubstringTwoDistinct(inp))