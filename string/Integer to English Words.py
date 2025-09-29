#Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^{31} - 1.

#reverse the string
# we should process it in sequences of 3 digits from billion to thousands recursively
# for hundereds we need another function:
#   if<100 : another function for two digits
#   otherwise


class Solution(object):

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
             9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen",
             16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
             50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        num = str(num)
        num = num[::-1]
        if(num=='0'):
            return "Zero"
        def ten(num):
            num = str(int(num))
            if (int(num) == 0):
                return ""
            if (int(num)) <= 20:
                return d[int(num)]
            elif (int(num) % 10 == 0):
                return d[int(num[0]) * 10]
            else:
                return d[int(num[0]) * 10] + " " + d[int(num[1])]

        def hundred(num):
            num = num[::-1]
            if (int(num) < 100):
                return ten(num)
            elif (int(num) % 100 == 0):
                return d[int(num[0])] + " Hundred"
            else:
                return d[int(num[0])] + " Hundred " + ten(num[1:])

        def rec(num):
            m = len(num)
            if (m <= 12 and m >= 10):
                a=hundred(num[9:]) + " Billion " + rec(num[:9]) if hundred(num[9:])!="" else rec(num[:9])
            elif (m <= 9 and m >= 7):
                a=hundred(num[6:]) + " Million " + rec(num[:6]) if hundred(num[6:])!="" else rec(num[:6])
            elif (m <= 6 and m >= 4):
                a=hundred(num[3:]) + " Thousand " + rec(num[:3]) if hundred(num[3:])!="" else rec(num[:3])
            else:
                a=hundred(num)
            return a
        print(rec(num).rstrip())
        return rec(num).rstrip()

num=1099
num=1000
num=1000000
num=1234567891
num=0
num=1000010
s=Solution()
s.numberToWords(num)