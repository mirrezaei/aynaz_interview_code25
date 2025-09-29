#Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

#In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

#Return true if and only if you can transform str1 into str2.


# if we can convert str1 to str1, then each char at str1 should be transfered to one and only one char, not more. If there are more then one transfer return False
# if the transfer map sounds fine regarding the above condition, then we need to make sure that the number of chars used in the str2 is less than 26, unless the two strings are equal
# we need to have less than 26 chars in str2; otherwise there is a loop in the transformation links and we cannot fix ot because we don't have any extra char to consider it as a tmp char and fix the loop
#if the number of chars is less than 26, then we can fix the loop (in case there exists) using a tmp char

#example: consider the alphabet set {a,b,c}:  str1:abc, str2:bac then:  a->b, b->a, c->c  we cannot fix it
#example: consider the alphabet set {a,b,c,d}:  str1:abc, str2:bac then:  a->d, b->a, d->b, c->c  we cannot fix it using the tmp char "d"

#idea: we create one dictionary and start adding the change plan
#when all the chars of our alphasbet are used in the str2, then it means that definitely there is a loop unless the two strings are equal
# if the number of chars in str2 are less than 26, then we are fine regardless of having a loop or not, because we can fix it in case there exists one


class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        d = {}
        if (str1 == str2):
            return True
        for i in range(len(str1)):
            if (str1[i] not in d):#only one transfer for each char
                d[str1[i]] = str2[i]
            else:
                if (str2[i] != d[str1[i]]):
                    return False
        print(len(d))
        print(len(set(str2)))
        return len(set(str2)) < 26# this is very important becaue it can detect if there is a loop or not

s=Solution()
str1="abcdefghijklmnopqrstuvwxyz"
str2="bcdefghijklmnopqrstuvwxyzq"
print(s.canConvert(str1,str2))
