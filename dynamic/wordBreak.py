#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

#solution is O(n^2)
#a[i]=  j<i    a[j] and s[j:i]
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        a = [False for i in range(len(s) + 1)]
        a[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if (a[j] == True and s[j:i ] in wordDict):
                    a[i] = True
                    break
        return a[-1]

st="leetcode"
dic=["leet","code"]
s=Solution()
print(s.wordBreak(st,dic))