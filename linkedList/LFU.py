#Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
import heapq

class LFUCache2(object):# the problem with this solution is that in case there are several the same keys, we cannot evict the least recently used

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.h = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i in range(len(self.h)):
            if (self.h[i][1] == key):
                self.h[i] = (self.h[i][0] + 1, self.h[i][1], self.h[i][2])
                v = self.h[i][2]
                heapq.heapify(self.h)
                return v
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for i in range(len(self.h)):
            if (self.h[i][1] == key):
                self.h[i] = (self.h[i][0] + 1, self.h[i][1], value)
                heapq.heapify(self.h)
                return
        if (len(self.h) >= self.cap and self.cap > 0):
            heapq.heappop(self.h)
        if (self.cap > 0):
            heapq.heappush(self.h, (1, key, value))


class LinkedList(object):
    def __init__(self, key, val, fre):
        self.key = key
        self.val = val
        self.fre = fre
        self.prev = None
        self.next = None


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.df = {}
        self.dk = {}
        self.count = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if (key in self.dk):
            elem = self.dk[key]
            n = elem.next
            p = elem.prev
            p.next = n
            if (n != None):
                n.prev = p
            elem.prev=None
            elem.next=None
            s, e = self.df[elem.fre]
            if(s.next==None):
                del self.df[elem.fre]
            elem.fre += 1
            if (elem.fre not in self.df):
                l = LinkedList("#", "", 0)
                self.df[elem.fre] = [l, l]
            s, e = self.df[elem.fre]
            e.next = elem
            elem.prev = e
            self.df[elem.fre][1] = elem

            return elem.val

        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if (key in self.dk):
            elem = self.dk[key]
            elem.val = value
            # first drop the elem from its old freq
            n = elem.next
            p = elem.prev
            p.next = n
            n.prev = p
            elem.fre += 1
            elem.prev = None
            elem.next = None
            self.count -= 1
        else:
            elem = LinkedList(key, value, 1)
            self.dk[key] = elem

        if (elem.fre not in self.df):
            l = LinkedList("#", "", 0)
            self.df[elem.fre] = [l, l]

        if (self.count >= self.cap):
            s, e = self.df[min(self.df)]
            first = s.next
            if(first!=None):
                n = first.next
            else:
                n=None
            if(first!=None):
                del self.dk[first.val]
            s.next = n
            if(n!=None):
                n.prev = s
            self.count -= 1
        s, e = self.df[elem.fre]
        e.next = elem
        elem.prev = e
        self.df[elem.fre][1] = elem
        self.count += 1


lfu=LFUCache(2)
lfu.put(1,1)
lfu.put(2,2)
lfu.get(1)
lfu.put(3,3)
lfu.get(2)
lfu.get(3)
lfu.put(4,4)
lfu.get(1)
lfu.get(3)
lfu.get(4)


