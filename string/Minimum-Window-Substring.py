#Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

#order of chard in T is not important
from collections import Counter

#idea: we starte traversing S, we know the number of chars is needed for T,
#we keep a dictionary from the nu of chars in string T
# we start traversing S and updating the nu of chars we have seen so far in the S
# as soon as we met all the needed chars, we have found the first window, we save the start and end and keep going

class Solution(object):
    def minWindow2(s, t):#BEST approach
        need = Counter(t)  # hash table to store char frequency
        missing = len(t)  # total number of chars we care
        start, end = 0, 0
        i = 0#start of the window
        for j, char in enumerate(s, 1):  # index j from 1
            if need[char] > 0:#one of the required chars have been seen
                missing -= 1
            need[char] -= 1# regardless of being required or not, we reduce its amount
            if missing == 0:  # match all chars # as soon as missing is equal to zero, it means we foundd a window
                while i < j and need[s[i]] < 0:  # try to minimize the window if possible, for example if we have seen many from a char lets move forward the beginning of the window
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1  #prepare for the next window# make sure the first appearing char satisfies need[char]>0
                missing += 1  # we missed this first char, so add missing by 1
                if end == 0 or j - i < end - start:  # update window
                    start, end = i, j
                i += 1  # update i to start+1 for next window
        return s[start:end]


s="ADOBECODEBANC"
t="ABC"

#s="bba"
#t="ab"
so=Solution()
print(so.minWindow(s,t))



