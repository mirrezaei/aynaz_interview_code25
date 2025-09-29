#You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

#Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        root = head
        stack = []# to add next when we have child
        while (head != None):
            ne = head.next
            ch = head.child
            if (head.child != None): # if we have child, we change child to head and add next to stack
                head.next = ch
                ch.prev = head
                head.child = None
                if (ne == None):
                    if (len(stack) > 0):
                        cur = stack.pop(-1)
                        head.next = cur
                        cur.prev = head
                        head = cur
                    else:
                        head = ch
                else:
                    stack.append(ne)
                    head = ch
            else:  # if we don't have child, we change next to head
                if (ne != None):
                    head = ne
                else:
                    if (len(stack) > 0):
                        cur = stack.pop(-1)
                        head.next = cur
                        cur.prev = head
                        head = cur
                    else:
                        break
        return root


