#!/bin/python3
#There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.

#For example, given input  and , we find  instances of ',  of '' and  of ''. For each query, we add an element to our return array, .

#Function Description

#Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

#matchingStrings has the following parameters:

#strings - an array of strings to search
#queries - an array of query strings
#Input Format

#The first line contains and integer , the size of .
#Each of the next  lines contains a string .
#The next line contains , the size of .
#Each of the next  lines contains a string .

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    hash={}
    for q in queries:
        hash[q]=0

    for s in strings:
        if(s in hash.keys()):
            hash[s]+=1
    final=[]
    for q in queries:
        final.append(hash[q])

    return final


if __name__ == '__main__':
    fptr = open('result.txt', 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
#2025