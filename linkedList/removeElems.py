# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Remove all elements from a linked list of integers that have value val.


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start=head
        prev=None
        while(start!=None):
            if(start.val==val):
                if(prev!=None):
                    prev.next=start.next
                    start=start.next
                else:
                    head=start.next
                    start=head
            else:
                prev=start
                start=start.next
        return head