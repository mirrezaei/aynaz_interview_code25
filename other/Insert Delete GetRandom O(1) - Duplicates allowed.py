#Design a data structure that supports all following operations in average O(1) time.

#Note: Duplicate elements are allowed.
#insert(val): Inserts an item val to the collection.
#remove(val): Removes an item val from the collection if present.
#getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.

import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = []
        self.d = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.a.append(val)
        if (val not in self.d):
            self.d[val] = set({len(self.a) - 1})
            return True
        else:
            self.d[val].add(len(self.a) - 1)
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        else:
            ind = self.d[val].pop()
            if(len(self.a)-1==ind):
                self.a.pop(-1)
            else:
                elem = self.a[-1]
                self.a[ind] = elem
                self.a.pop(-1)
                self.d[elem].remove(len(self.a))
                self.d[elem].add(ind)
            if (len(self.d[val]) == 0):
                del self.d[val]
            return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        r = random.randint(0, len(self.a) - 1)
        return self.a[r]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
s=RandomizedCollection()
s.insert(9)
s.insert(9)
s.remove(1)
s.insert(1)
s.insert(2)
s.insert(1)
s.remove(2)
s.remove(1)
s.remove(1)
s.insert(9)
s.remove(1)