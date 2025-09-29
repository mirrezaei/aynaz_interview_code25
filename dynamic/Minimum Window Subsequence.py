#Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.
#If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.



# the idea is that for each char in T starts
#we need to create an array a with len(T) * len(S)
#a[i][j]: if we want to cover substring T[:i+1] , how many chars we need to go back from index j in string S
#the final result is the min numer in last row of the a
#however, at each row we only need the previous row, so we careat a two row matrix and continue the above logic



class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        a = [[float('inf')] * len(S) for i in range(2)]

        w = float('inf')#length of window
        ind = -1
        for j in range(len(S)): # first row (first char of T) # a[0][j]: how many char we needd to go back from inddex j in sting S to cover the first character of string T
            if (S[j] == T[0]):
                a[0][j] = 1
                if(len(T)==1 and a[0][j]<w):
                    w = 1
                    ind = j
            else:
                if(j==0):
                    a[0][0]=float('inf')
                else:
                    a[0][j]=a[0][j-1]+1
        for i in range(1,len(T)):# for ith char in T we need to  see if there is a substring in S that covers T[:i+1]
            for j in range(1, len(S)):
                if (T[i] == S[j] ):
                    a[1][j] = min(a[0][j-1]+1, a[1][j - 1] + 1)

                else:
                    a[1][j] = a[1][j - 1] + 1
                if (i == len(T) - 1 and a[1][j] < w):#find the min window
                    w = a[1][j]
                    ind = j
            a[0] = a[1][:]
            a[1][0]=float('inf')
        return "" if ind == -1 else S[ind - w + 1:ind + 1]

s=Solution()
S = "abcdebdde"
T = "bde"

#S="cnhczmccqouqadqtmjjzl"
#T="mm"

#S="fweekpamjwqobhxiesgzivminqqjjkgnhkdxpfjvvgfcdlgwvwtdwizpjcuwnwpioxcshyjglqjnkluedopzyhozjzqnjentspwffoawwbgyhrrapncwetqulmaupkkwugkpfztgejujlakrnkvefbvncfzhhmciztzjzrzrzlcfkejmlkhlogtraexhgrvxitcnaacegjrkwbseomwvdawsymemhsvtqcpbfvinhngdvhnrswwgoff"
#T="qkkwtlzbbn"

print(s.minWindow(S,T))
