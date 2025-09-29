#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

#'.' Matches any single character.
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).

#Note:

#s could be empty and contains only lowercase letters a-z.
#p could be empty and contains only lowercase letters a-z, and characters like . or *.

#a (len(p)+1,len(s)+1)
#a[i][j]: if we can produce the string s until position j using the first i chars of pattern p
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        a = [[False] * (len(s) + 1) for i in range(len(p) + 1)]
        a[0][0] = True
        for i in range(len(p)):
            if (p[i] == "*" and i - 1 >= 0):
                a[i + 1][0] = a[i - 1][0]

        print(a)

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if (p[i - 1].isalpha()):
                    a[i][j] = a[i - 1][j - 1] and (p[i - 1] == s[j - 1])
                elif (p[i - 1] == "*"):
                    if (i - 2 >= 0):
                        a[i][j] = a[i - 2][j] or ((a[i - 1][j - 1] or a[i][j - 1]) and (p[i - 2] == s[j - 1] or p[i-2]=="."))
                elif (p[i - 1] == "."):
                    a[i][j] = a[i - 1][j - 1]
        for i in range(len(a)):
            print(a[i])
        return a[len(p)][len(s)]


so=Solution()
s = "aab"
p = "c*a*b"

s = "aa"
p = "a"

s = "aa"
p = "a*"

s = "mississippi"
p = "mis*is*p*."

#s = "ab"
#p = ".*"
print(so.isMatch(s,p))