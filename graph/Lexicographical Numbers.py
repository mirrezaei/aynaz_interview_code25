#Given an integer n, return 1 - n in lexicographical order.

#For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

#Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

class Solution(object):#solution is implementation of DFS
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        stack = []
        out = []
        for i in range(1, 10):
            if (i <= n):
                stack.append(str(i))
                while (len(stack) > 0):
                    cur = stack.pop(-1)
                    out.append(int(cur))
                    for j in range(9, -1, -1):
                        if (int(cur + str(j)) <= n):
                            stack.append(cur + str(j))
        return out



