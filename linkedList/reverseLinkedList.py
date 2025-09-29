#Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None):
            return None
        elif(head.next==None):
            return head
        else:
            prev=None
            while(head.next!=None):
                cur=head
                ne=head.next
                cur.next=prev
                prev=cur
                head=ne
            head.next=prev
        return head
