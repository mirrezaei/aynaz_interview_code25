#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Note: For the purpose of this problem, we define empty string as valid palindrome.

#Example 1:

#Input: "A man, a plan, a canal: Panama"
#Output: true
#Example 2:

#Input: "race a car"
#Output: false
class Solution(object):
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        out = []
        for c in s:
            if c.isalpha() or c.isdigit():
                out.append(c.lower())
        n = len(out) - 1
        for i in range(len(out) / 2):
            if (out[i] != out[n - i]):
                return False
        return True

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while (l < r):
            while (s[l].isalpha() == False and s[l].isdigit() == False and l < r):
                l += 1
            while (s[r].isalpha() == False and s[r].isdigit() == False and l < r):
                r -= 1
            if (s[r].lower() != s[l].lower()):
                return False
            l+=1
            r-=1
        return True

so=Solution()
s="A man, a plan, a canal: Panama"
so.isPalindrome(s)
