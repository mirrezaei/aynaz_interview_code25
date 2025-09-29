#Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

#

class Solution(object):
    # A[i][j]: using i chars from the s1 and j chars from the s2, if we are able to reconstruct the i+j chars from s3
    def isInterleave2(self, s1, s2, s3):#BEST approach
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        def check(ind_s3, ind_s, s):
            if (ind_s < 0 or ind_s3 > len(s3)):
                return False
            elif (s3[ind_s3 - 1] == s[ind_s]):
                return True
            else:
                return False

        a = [[False for j in range(len(s2) + 2)] for i in range(len(s1) + 2)]  # dim: len(s1)+2 * len(s2)+2
        for i in range(1, len(s1) + 2):
            for j in range(1, len(s2) + 2):
                if (i == 1 and j == 1):
                    a[1][1] = True
                else:
                    a[i][j] = (a[i - 1][j] and check(j - 1 + i - 1, i - 2, s1)) or (
                                a[i][j - 1] and check(i - 1 + j - 1, j - 2, s2))
        print(a)
        return (a[len(s1) + 1][len(s2) + 1] and (len(s3) == len(s1) + len(s2)))
    def isInterleave(self, s1, s2, s3):#correct approach, but it is brute force search and it cannot pass all the test cases considering the time complexity
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if (s1 == "" and s2 == "" and s3 == ""):
            return True
        elif (s3 == "" and (s1 != "" or s2 != "")):
            return False
        elif (len(s3) > 0 and s2 == "" and s1 == ""):
            return False
        else:
            if (s1 == ""):
                if (s3[0] == s2[0]):
                    return self.isInterleave("", s2[1:], s3[1:])
                else:
                    return False
            elif (s2 == ""):
                if (s3[0] == s1[0]):
                    return self.isInterleave(s1[1:], "", s3[1:])
                else:
                    return False
            else:
                if (s3[0] == s1[0] and s3[0] == s2[0]):
                    return (self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:]))
                elif (s3[0] == s1[0]):
                    return self.isInterleave(s1[1:], s2, s3[1:])
                elif (s3[0] == s2[0]):
                    return self.isInterleave(s1, s2[1:], s3[1:])
                else:
                    return False


s=Solution()
s.isInterleave2("","","a")