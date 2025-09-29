#Implement atoi which converts a string to an integer.

#The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

#The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

#If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

#If no valid conversion could be performed, a zero value is returned.

#Note:

#Only the space character ' ' is considered as whitespace character.
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if (str == ""):
            return 0
        minus = False
        for i in range(len(str)):
            if (str[i].isdigit() == False and str[i].isspace() == False and str[i] != "-" and str[i] != "+"):
                return 0
            elif (str[i] == "-"):
                minus = True
                i+=1
                break
            elif (str[i] == "+"):
                i+=1
                break

            elif (str[i].isspace() == False):
                break
        num = 0
        for j in range(i, len(str)):
            if (str[j].isdigit()):
                num = num * 10 + int(str[j])
                if (minus == False and num > 2 ** 31 - 1):
                    return 2 ** 31 - 1
                if (minus == True and num > 2 ** 31):
                    return -(2 ** 31)
            else:
                break

        return -num if minus else num

s=Solution()
st= "   -42"
st="4193 with words"
st="words and 987"
st="+-2"
st="+1"
st=""
print(s.myAtoi(st))