class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for c in s:
            if (c == "["):
                stack.append("[")
            elif (c == "]"):
                if (len(stack) == 0):
                    return False
                elif (stack[-1] == "["):
                    del stack[-1]
                else:
                    return False
            elif (c == "{"):
                stack.append("{")
            elif (c == "}"):
                if (len(stack) == 0):
                    return False
                elif (stack[-1] == "{"):
                    del stack[-1]
                else:
                    return False
            elif (c == "("):
                stack.append("(")
            else:
                if (len(stack) == 0):
                    return False
                elif (stack[-1] == "("):
                    del stack[-1]
                else:
                    return False
        if (len(stack) == 0):
            return True
        else:
            return False


    def isValid2(self, s):# A very clean code
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