#Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

#sNote that after backspacing an empty text, the text will continue empty.

#idea is that to process from right to left, and have pointers to two strings. when we see # we skip, and we compare char by char
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


class Solution3(object): #best and simple
    def backspaceCompare(s: str, t: str) -> bool:
        def next_valid_char_index(string, index): # this function gets the index and adjust it depending on seeing/ not seeing the #
            skip = 0
            while index >= 0:
                if string[index] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    break
                index -= 1
            return index

        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            i = next_valid_char_index(s, i)
            j = next_valid_char_index(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True


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



