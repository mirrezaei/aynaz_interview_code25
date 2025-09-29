#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution(object):
    def valid(self, s):
        count = 0
        for c in s:
            if (c == "("):
                count += 1
            elif (c == ")"):
                count -= 1
                if count < 0:
                    return False, count
        return True, count

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = set()
        q = []
        n_open = 0
        n_close = 0
        q.append(["(", 1, 0])
        n_open += 1
        while (len(q) > 0):
            e = q.pop(0)
            s = e[0]
            n_open = e[1]
            n_close = e[2]
            validity, co = self.valid(s)
            if (n_open == n and n_close == n and validity == True and co == 0):
                out.add(s)
                print(s)
            if (validity):
                if (n_close < n):
                    q.append([s + ")", n_open , n_close+1])
                if (n_open < n):
                    q.append([s + "(", n_open+1, n_close ])
        print(out)
        return list(out)

    def generateParenthesis2(self, n): #more clean approach
        """
        :type n: int
        :rtype: List[str]
        """
        out = set()
        q = []
        n_open = 0
        n_close = 0
        q.append(["(", 1, 0])
        n_open += 1
        while (len(q) > 0):
            e = q.pop(0)
            s = e[0]
            n_open = e[1]
            n_close = e[2]
            if (n_open == n  and n_close-n_open== 0):# correct and complete
                out.add(s)
                print(s)
            if (n_open>=n_close):#otherwise it is wrong
                if (n_close < n):
                    q.append([s + ")", n_open , n_close+1])
                if (n_open < n):
                    q.append([s + "(", n_open+1, n_close ])
        print(out)
        return list(out)



s=Solution()
s.generateParenthesis2(3)