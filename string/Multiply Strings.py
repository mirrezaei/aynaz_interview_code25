#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
class Solution(object):
    def multiply(self,num1, num2):
        s=[0 for _ in range(len(num1+num2))]#maximum possible length is len(num1)+len(num2)
        pos=len(s)-1
        curPos=pos
        carry=0
        for c1 in reversed(num1):
            for c2 in reversed(num2):
                tm=int(c1)*int(c2)+carry+s[curPos]
                s[curPos]=tm%10#reminder
                carry=tm/10
                curPos-=1
            if(carry>0):
                s[curPos]+=carry
            pos-=1
            curPos=pos
            carry=0
        i=0
        while(i<len(s)-1 and s[i]==0):#remove zero from beginning
            i+=1


        print("".join(str(e) for e in s[i:]))







s=Solution()
num1 = "123"
num2 = "456"

#num1 = "9"
#num2 = "9"

num1 = "0"
num2 = "0"
print(s.multiply(num1,num2))