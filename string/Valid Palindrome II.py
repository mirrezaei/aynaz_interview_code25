#Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

class Solution(object):
    def check(self, s):
        return all(s[i] == s[len(s) - 1 - i] for i in range(len(s) / 2))

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while (l < r):
            if (s[l] != s[r]):
                return self.check(s[l + 1:r + 1]) or self.check(s[l: r])

            l += 1
            r -= 1
        return True


s="abca"
s="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
so=Solution()
print(so.validPalindrome(s))