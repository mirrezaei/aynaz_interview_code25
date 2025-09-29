#A message containing letters from A-Z is being encoded to numbers using the following mapping:

#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given a non-empty string containing only digits, determine the total number of ways to decode it.
class Solution(object):
    def numDecodings2(self, s):# this is a general approach for when the value of the dictionary d may be numbers with any length of the digits
        """
        :type s: str
        :rtype: int
        """
        def checkZero(inp):
            if (inp[0] == "0"):
                return False
            else:
                return True

        d = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
             14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
             26: 'Z'}
        if (len(s) == 1):
            if (int(s) in d):
                return 1
            else:
                return 0
        arr = [0 for i in range(len(s))]
        if (int(s[0]) in d):
            arr[0] = 1
        for i in range(1, len(s)):
            if (int(s[i]) in d and s[i - 1] == 1):
                arr[i] = 1
        for j in range(2, len(s) + 1):
            for i in range(j - 1, len(s)):
                sum = 0
                for k in range(i - j, i):
                    if (k == -1):
                        print(s[0:i + 1])
                        if (int(s[0:i + 1]) in d and checkZero(s[0:i + 1])):
                            sum += 1
                    else:
                        print(s[k + 1:i + 1])
                        if (int(s[k + 1:i + 1]) in d and checkZero(s[k + 1:i + 1])):
                            sum += arr[k]
                arr[i] = sum
            print(arr)
        return arr[-1]

    def numDecodings(self, s):# p refers to the previous number, pp refers to the previous of the previous
        """
        :type s: str
        :rtype: int
        """

        final=0# the total numer of ways we can decode so far,
        p=0
        pp=1
        if(len(s)==0):
            return 0
        if(len(s)>=1):
            if(s[0]=="0"):
                return 0
            else:
                p=1
            final=p
        for i in range(1,len(s)):
                if(s[i]=="0"):
                    if (s[i-1] == "1" or s[i-1] == "2"):
                        final=pp
                        pp=0
                        p=final
                    else:
                        return 0
                else:
                    if (s[i-1] == "1" or (s[i-1] == "2" and int(s[i]) <= 6)):
                        final = p + pp
                    else:
                        final=p
                    pp=p
                    p=final

        return final





s=Solution()
print(s.numDecodings("12345"))