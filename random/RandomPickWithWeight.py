import random


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        interval = 0
        for i in range(len(self.w)):
            interval += self.w[i]
            self.w[i] = interval

    def pickIndex(self):
        """
        :rtype: int
        """
        r = random.randint(0,self.w[-1]-1)
        def binary( left, right):
            if (right - left == 0):
                return right
            elif (right - left == 1):
                if (r < self.w[left]):
                    return left
                else:
                    return right
            else:
                m = (right - left) / 2
                if (r < self.w[m + left]):
                    return binary( left, left + m)
                else:
                    return binary( left + m + 1, right)
        ind = binary( 0, len(self.w) - 1)
        return ind

# Your Solution object will be instantiated and called as such:
w=[3,14,1,7]
obj = Solution(w)
for i in range(500):
    param_1 = obj.pickIndex()
    print(param_1)