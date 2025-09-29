import sys


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (len(self.a) == 0):
            self.a.append((x, x))
        else:
            if (x < self.a[-1][1]):
                self.a.append((x, x))
            else:
                self.a.append((x, self.a[-1][1]))

    def pop(self):
        """
        :rtype: None
        """
        x = self.a.pop(-1)
        return x[0]

    def top(self):
        """
        :rtype: int
        """
        return self.a[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.a[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()