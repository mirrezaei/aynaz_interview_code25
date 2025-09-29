#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def cycle(pt1,pt2):
    if(pt1==pt2):
        return 1
    elif pt1==None:
        return 0
    elif pt2==None:
        return 0
    else:
        if(pt1.next!=None):
            pt1 = pt1.next
            if(pt2.next!=None):
                if(pt2.next.next!=None):
                    pt2 = pt2.next.next
                    res=cycle(pt1, pt2)
                    return res
                else:
                    return 0
            else:
                return 0
        else:
            return 0


def has_cycle(head):
    pt1=head
    pt2=head
    if(head==None):
        return 0
    else:
        if(head.next!=None):
            if(head==head.next):
                return 1
            else:
                pt1=pt1.next
                if(head.next.next!=None):
                    pt2=pt2.next.next
                    res=cycle(pt1,pt2)
                    return res
                else:
                    return 0
        else:
            return 0

if __name__ == '__main__':

    list=SinglyLinkedList()
    list.insert_node(1)
    list.insert_node(2)
    list.insert_node(3)
    list.insert_node(4)
    list.insert_node(5)
    list.tail.next=list.head.next.next
    aynaz=has_cycle(list.head)
    print(aynaz)