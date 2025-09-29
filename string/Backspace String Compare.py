#Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

#sNote that after backspacing an empty text, the text will continue empty.

import itertools
class Solution2(object):
    def backspaceCompare(self, S, T):
        def F(s):
            skip=0
            for ch in s:
                if ch=="#":
                    skip+=1
                elif skip>0:
                    skip-=1
                else:
                    yield ch

        return all(x==y for x,y in itertools.izip_longest(F(S),F(T)))


class Solution3(object):
    def backspaceCompare(self, S, T):
        i = len(S) - 1
        j = len(T) - 1
        counts = 0
        countt = 0
        while (i >= 0 or j >= 0):
            if (i >= 0 and S[i] == "#"):
                counts += 1
                i -= 1
                while ((counts > 0 or S[i]=="#") and i >= 0):
                    if (S[i] == "#"):
                        counts += 1
                    else:
                        counts -= 1
                    i -= 1

            if (j >= 0 and T[j] == "#"):
                countt += 1
                j -= 1
                while ( (countt > 0 or T[j]=="#") and j >= 0):
                    if (T[j] == "#"):
                        countt += 1
                    else:
                        countt -= 1
                    j -= 1
            if i >= 0 and j >= 0 and S[i] == T[j]:
                i -= 1
                j -= 1
            elif(i<0 and j<0):
                return True
            else:
                return False

        return True if i <0 and j<0 else False


class Solution(object):

    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def process(l):
            k = len(l) - 1
            count = 1
            while (k > -1 and l[k] == "#"):
                k -= 1
                count += 1
            return k, count

        def skip(l, k, count):
            while ((count > 0 or l[k]=="#") and k > -1):
                if l[k] != "#":
                    k -= 1
                    count-=1
                else:
                    k -= 1
                    count += 1
            return k,count

        i = len(s) - 1
        j = len(t) - 1
        while (i >= 0 or j >= 0):
            if i>-1 and s[i] == "#":
                i, count_s = process(s[:i])
                if count_s > 0:
                    i,count_s = skip(s, i, count_s)
            if j>-1 and t[j] == "#":
                j, count_t = process(t[:j])
                if count_t > 0:
                    j,count_t = skip(t, j, count_t)
            if i == -1 and j == -1:
                return True
            else:
                if s[i] != t[j]:
                    return False
                else:
                    i -= 1
                    j -= 1
        if i == -1 and j == -1:
            return True
        else:
            return False


so=Solution()
S = "ab#c"
T = "ad#c"

S = "ab##"
T = "c#d#"

S="xywrrmp"
T="xywrrmu#p"

S="nzp#o#g"
T="b#nzp#o#g"

#S = "a#c"
#T = "b"

#S="bxj##tw"
#T="bxj###tw"


#S="ab##"
#T="c#d#"

#S="rheyggodcclgstf"
#T="#rheyggodcclgstf"
print(so.backspaceCompare(S,T))



