#Merge k Sorted Lists
import heapq#it is a minheap


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Element(object):
    def __init__(self,node,listNu):
        self.node=node
        self.listNu=listNu
    def __cmp__(self, other):
        return cmp(self.node.val, other.node.val)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap=[]
        first=[]
        k=len(lists)
        if(k>0): #if there is any lists
            for i in range(k):
                element=Element(lists[i],i)
                if(element.node!=None): #if the list is not empty
                    heapq.heappush(heap,element)
                    lists[i]=lists[i].next


            if(len(heap)>0): #if there is any element in the heap
                element=heapq.heappop(heap)
                first=element.node
                sorted = element.node

        while(len(heap)>0):
            newElement=Element(lists[element.listNu],element.listNu)
            if(newElement.node!=None):
                heapq.heappush(heap,newElement)
                lists[element.listNu]=lists[element.listNu].next
            element = heapq.heappop(heap)
            sorted.next = element.node
            sorted=element.node
        while(first!=None):
            print(str(first.val)+" ")
            first=first.next

        return first





node1=ListNode(2)
node2=ListNode(5)
node3=ListNode(8)
node1.next=node2
node2.next=node3

mode1=ListNode(1)
mode2=ListNode(3)
mode3=ListNode(7)
mode1.next=mode2
mode2.next=mode3

kode1=ListNode(4)
kode2=ListNode(6)
kode3=ListNode(9)
kode1.next=kode2
kode2.next=kode3

s=Solution()
s.mergeKLists([node1,mode1, kode1])