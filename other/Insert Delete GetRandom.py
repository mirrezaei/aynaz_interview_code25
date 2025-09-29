#Design a data structure that supports all following operations in average O(1) time.

#insert(val): Inserts an item val to the set if not already present.
#remove(val): Removes an item val from the set if present.
#getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.a = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if (val not in self.d):
            self.a.append(val)
            self.d[val] = len(self.a) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if (val in self.d):
            ind = self.d[val]
            self.a[ind] = self.a[-1]
            self.d[self.a[-1]] = ind
            del self.a[-1]
            del self.d[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if (len(self.a) == 0):
            return False
        r = random.randint(0, len(self.a) - 1)
        return self.a[r]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()