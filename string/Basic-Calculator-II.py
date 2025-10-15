#Implement a basic calculator to evaluate a simple expression string.

#The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.


#idea is that before processing the number we save its sign (pos or neg)
# for the first number we keep sign positive by default
#if we see + or - we append  positive or negative number to the stack
# if we see * or / we pop the last number from stack and do the peration and append the results
# finally we add all the remaining numbers in the stack
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        num = 0
        sign = '+'
        i = 0

        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num))  # Truncate toward zero

                sign = ch
                num = 0

            i += 1

        # Manually sum the stack
        result = 0
        for val in stack:
            result += val

        return result
class Solution2(object):

    def calculate(self, s):#if + or - we add to stack; if * or / we shoudl pop from stack, calculate and push it again
        """
        :type s: str
        :rtype: int
        """
        stack = []
        pri = False
        i = 0
        while i < len(s):
            if (s[i].isdigit()):
                n = s[i]
                i += 1
                while (i<len(s) and s[i].isdigit()):
                    n += s[i]
                    i += 1
                if (pri == False):
                    stack.append(int(n))
                else:
                    op = stack.pop(-1)
                    nextNu = stack.pop(-1)
                    pri = False
                    if (op == "*"):
                        stack.append(nextNu * int(n))
                    elif (op == "/"):
                        stack.append(nextNu / int(n))
            elif (s[i] == "+" or s[i] == "-"):
                stack.append(s[i])
                i += 1
            elif (s[i] == "/" or s[i] == "*"):
                stack.append(s[i])
                pri = True
                i+=1
            else:
                i += 1

        stack.reverse()#**********IMPORTANT
        nu1 = stack.pop(-1)
        while (len(stack) > 0):
            op = stack.pop(-1)
            nu2 = stack.pop(-1)
            if(op == "-" ):
                nu1 = nu1 - nu2
            if (op == "+"):
                nu1 = nu2 + nu1
        print(nu1)
        return nu1







s=Solution()
input="3-2*2"
#input="1-1+1"
input="14-3/2"
print(s.calculate(input))