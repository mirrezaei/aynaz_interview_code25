class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = ""
        stack = []
        i=0
        while (i < len(s)):
            if s[i].isdigit():
                q = []
                num=""
                while (i < len(s)):
                    if (s[i].isdigit()):
                        num = num + s[i]
                        i += 1
                    else:
                        break
                q.append(int(num))
            elif(s[i]=="["):
                t = ""
                i+=1
                while (i < len(s)):
                    if (s[i].isalpha()):
                        t = t + s[i]
                        i += 1
                    else:
                        break
                q.append(t)
                stack.append(q)

            elif (s[i] == "]"):
                cur = stack.pop(-1)
                t = ""
                for j in range(cur[0]):
                    t = t + cur[1]
                if (len(stack) > 0):
                    stack[-1][1] = stack[-1][1] + t
                else:
                    out = out + t
                i += 1
            elif (s[i].isalpha()):
                if (len(stack) > 0):
                    stack[-1][1] = stack[-1][1] + s[i]
                else:
                    out = out + s[i]
                i+=1
        print(out)
        return out




s=Solution()
s.decodeString("3[a]2[bc]")
s.decodeString("3[a2[c]]")
s.decodeString("2[abc]3[cd]ef")