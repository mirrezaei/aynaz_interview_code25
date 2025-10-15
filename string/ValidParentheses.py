#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.


#the idea is that we push the open paranthesis in the stack
#and when we see a closed one , we pop from the stack, the poped one and the closed one should be from the same type
class Solution(object):
    def isValid(self, s):# A very clean code
        stack = []
        d={")":"(","}":"{","]":"["}
        for c in s:
            if c in d.keys():# pop if ut is closed
                if (len(stack) == 0):
                    return False
                else:
                    l=stack.pop(-1)
                    if(l!=d[c]):
                        return False
            else:
                stack.append(c)# appendd if it is open bracket
        if (len(stack) == 0):
            return True
        else:
            return False



s=Solution()
a="("
print(s.isValid(a))