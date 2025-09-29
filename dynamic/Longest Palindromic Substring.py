#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#a[i][j]: the length of the palindrome string that ends at positin j with length i+1
class Solution(object):


    def longestPalindrome(self, s):  # BEST time o(n^2), space:O(1)
        if(len(s)==0):
            return ""
        longest=(1,s[0])
        for i in range(2*len(s)):#consider 2*len(s), just to make it easier to check even and odd palindromes
            if(i%2==0):
                l=self.check(s,i/2)#if the palindrom string is even
            else:
                l = self.check2(s, i/2,i/2+1)# if the palindrom string is odd
            if (l[0] > longest[0]):
                longest = l
        return longest[1]


    def check(self,s,k):
        m=1
        long=(1,s[k])
        while(k+m<len(s) and k-m>=0):
            if(s[k+m]==s[k-m]):
                long=(long[0]+2,s[k-m:k+m+1])
            else:
                break
            m+=1
        return long

    def check2(self,s,i,j):
        long=(0,"")
        while(j<len(s) and i>=0):
            if(s[i]==s[j]):
                long=(long[0]+2,s[i:j+1])
            else:
                break
            i-=1
            j+=1
        return long

    def longestPalindrome2(self, s):#time o(n^2), space:O(n^2)
        """
        :type s: str
        :rtype: str
        """
        if (len(s) == 0):
            return ""
        a = [[0] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            a[0][i] = 1
        longest = (1, s[0])
        for i in range(1, len(s)):
            for j in range(i, len(s)):
                if (s[j] == s[j - i] and i - 2 >= 0 and a[i - 2][j - 1] > 0):
                    a[i][j] = a[i - 2][j - 1] + 2
                elif (s[j] == s[j - i] and i - 2 < 0):
                    a[i][j] = 2
                if (a[i][j] > longest[0]):
                    longest = (a[i][j], s[j - i:j + 1])
        return longest[1]






so=Solution()
inp="babad"
#inp="cbbd"
print(so.longestPalindrome(inp))