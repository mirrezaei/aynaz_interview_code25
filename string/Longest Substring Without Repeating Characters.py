#Given a string, find the length of the longest substring without repeating characters.

# the whole idea: we create a dict to keep the last occurrence of our distinct chars

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s == ""):
            return 0
        pivot = 0#start of substring
        d = {}
        d[s[0]] = 0# the last occurrence of a char
        maxLen = 1
        curLen = 1
        for i in range(1, len(s)):
            if (s[i] not in d):
                curLen += 1
            else:
                if (d[s[i]] < pivot):#the last occurrence of current char is before start of the substring
                    curLen += 1
                else:
                    pivot = d[s[i]] + 1#update the start of substring
                    curLen = i - pivot + 1#update the length of substring
            d[s[i]] = i#update the last ocurrence of substring
            if (curLen > maxLen):
                maxLen = curLen
        return maxLen


s=Solution()
inp="abcabcbb"
inp="bbbbb"
inp="pwwkew"
print(s.lengthOfLongestSubstring(inp))