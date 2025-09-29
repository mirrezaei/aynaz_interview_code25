#Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

#Note: The input string may contain letters other than the parentheses ( and ).


#points: BFS, huristic to remove strings that are wrong for further processing , no stack, counter is enogh
#idea: we start by removing one paranthesis at a time
# if the string has len of m, we first remove one char from that and check its validity, if it is valid we add it to the output and if not we try to remove another char
#at each step that we remove one char, we check if its open paranthesis is greater than close paranthesis or not, if it is not we don't continue trying that string anymore
#at each step that we remove one char, we also keep track of reducted string and number of open and close paranthesis

import sys
import collections
class Solution(object):

    def validity(self, s):

        counter=0
        for i in range(len(s)):
            if (s[i] == "("):
                counter+=1
            elif (s[i] == ")"):
                if (counter < 0):
                    return False
                elif (counter>0):
                    counter-=1
                else:
                    return False

        if(counter>0):
            return False

        return True

    def traverse(self, q, out):
        seen={}
        level = 100000# maximum number of paranthesis removalss
        while (len(q) > 0):
            s = q[0][0]#current string
            l = q[0][1]#nu of removals
            if (l > level):
                break
            del q[0]
            val = self.validity(s)
            if (val == True):
                level = l
                out.add(s)
            else:
                l_child=0
                r_child=0
                for i in range(len(s)):#at each time, remove one of the paranthesis
                    tem = list(s)
                    if(tem[i] == "(" or tem[i] == ")"):
                        a=tem[i]
                        if (r_child > l_child  ):#THIs is very important ********************************************n(if coles paranthesis is more than open paranthesis) __> wrong, don't continue
                            break
                        cur=tem[i]
                        del tem[i]
                        tem = ''.join(tem)
                        if(tem not in seen.keys()):#if we have reviewed this strig or not
                            q.append((tem, l + 1))
                            seen[tem]=0
                        if (cur == '('):
                            l_child+=1
                        else:
                            r_child+=1
        print(out)
        return out

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        d[1] = False
        out = set()
        q = [(s, 0)]
        self.traverse(q, out)
        return out

so=Solution()
ss=")((())((())(((f)()("
so.removeInvalidParentheses(ss)


