#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def sumDig(self, a1, a2, car):
        t = a1 + a2 + car
        if (t < 9):
            c = ListNode(t)
            car = 0
        else:
            rem = t % 10
            car = int(t / 10)
            c = ListNode(rem)
        return c, car

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1 = l1
        s2 = l2
        first = True
        root = None
        carry = 0
        while (s1 != None or s2 != None):
            if (s1 != None and s2 != None):
                c, carry = self.sumDig(s1.val, s2.val, carry)
                if (first == True):
                    root = c
                    curr = c
                    first = False
                else:
                    curr.next = c
                    curr = c
                s1 = s1.next
                s2 = s2.next
            elif (s1 == None):
                c, carry = self.sumDig(s2.val, 0, carry)
                curr.next = c
                curr = c
                s2 = s2.next
            else:
                c, carry = self.sumDig(s1.val, 0, carry)
                curr.next = c
                curr = c
                s1 = s1.next
        if (carry != 0):
            c = ListNode(1)
            curr.next = c
        return root


