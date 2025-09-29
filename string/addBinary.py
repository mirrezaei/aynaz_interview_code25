#Given two binary strings, return their sum (also a binary string).

#The input strings are both non-empty and contains only characters 1 or 0.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        out = ""
        while (i >= 0 or j >= 0):
            if (i < 0):
                s = int(b[j]) + carry
            elif (j < 0):
                s = int(a[i]) + carry
            else:
                s = int(a[i]) + int(b[j]) + carry
            if (s == 2):
                c = 0
                carry = 1
            elif (s == 3):
                c = 1
                carry = 1
            else:
                c = s
                carry = 0
            out = str(c) + out
            i -= 1
            j -= 1
        if (carry == 1):
            out = "1" + out
        return out

    def addBinary(self, a, b):# general
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        s = ""
        while (i > -1 and j > -1):
            sum = int(a[i]) + int(b[j]) + carry
            carry = sum / 2
            l = sum % 2
            s = s + str(l)
            i -= 1
            j -= 1
        if i > -1:
            cur = a
            ind = i
        else:
            cur = b
            ind = j
        while ind > -1:
            sum = int(cur[ind]) + carry
            carry = sum / 2
            l = sum % 2
            s = s + str(l)
            ind -= 1
        if carry > 0:
            s = s + str(carry)
        s = s[::-1]
        return s

    def addBinary(self, a, b): #general and best
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=a[::-1]
        b=b[::-1]
        carry=0
        s=""
        i=0
        while (i<min(len(a),len(b))):
            sum=int(a[i])+int(b[i])+carry
            carry=sum/2
            l=sum%2
            s=s+str(l)
            i+=1
        cur=a if i<len(a) else b
        while i<len(cur):
            sum=int(cur[i])+carry
            carry=sum/2
            l=sum%2
            s=s+str(l)
            i+=1
        if carry>0:
            s=s+str(carry)
        s=s[::-1]
        return s









