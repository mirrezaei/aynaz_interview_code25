#A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

#Return a deep copy of the list.

# Definition for a Node.

#Input:
#{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random



class Solution(object):
    def traverse(self, no, d):
        if (no.next != None):
            if (no.next not in d.keys()):
                temp = Node(no.next.val, None, None)
                d[no.next] = temp
                ne, rn = self.traverse(no.next, d)
                temp.next = ne
                temp.random = rn
                nextEl = temp
            else:
                nextEl = d[no.next]
        else:
            nextEl = None
        if (no.random != None):
            if (no.random not in d.keys()):
                temp = Node(no.random.val, None, None)
                d[no.random] = temp
                ne, rn = self.traverse(no.random, d)
                temp.next = ne
                temp.random = rn
                randomEl = temp
            else:
                randomEl = d[no.random]
        else:
            randomEl = None
        return nextEl, randomEl

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        d = {}
        if (head != None):
            root = Node(head.val, None, None)
            d[head] = root
            ne, rn = self.traverse(head, d)
            root.next = ne
            root.random = rn
        else:
            root = None
        return root

