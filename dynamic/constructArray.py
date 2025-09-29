#!/bin/python3

#Your goal is to find the number of ways to construct an array such that consecutive positions contain different values.

#Specifically, we want to construct an array with  elements such that each element between  and , inclusive. We also want the first and last elements of the array to be  and .

#Given ,  and , find the number of ways to construct such an array. Since the answer may be large, only find it modulo .

#For example, for , , , there are  ways, as shown here:

#image

#Complete the function countArray which takes input ,  and . Return the number of ways to construct the array such that consecutive elements are distinct.

#Constraints

#Subtasks

#For  of the maximum score,  and
#Sample Input

#, ,

#Sample Output


#Explanation

#Refer to the diagram in the challenge statement.

import math
import os
import random
import re
import sys

# Complete the countArray function below.
def fillArray(a,j): # recursive approach in order of (k-1)^(n-2) or in other words k^n
    if(j==n-1):
        if(a[j]!=a[n-2]):
            return 1
        else:
            return 0
    else:
        c=0
        for i in range(k):
            if(a[j-1]!=i+1):
                a[j]=i+1
                c=c+fillArray(a,j+1)
        return c%(10^9+7)


def countArray2(n, k, x):#in order of (k-1)^(n-2) or in other words k^n
    # Return the number of ways to fill in the array.
    a=[0 for i in range(n)]
    a[0]=1
    a[n-1]=x
    final=fillArray(a,j=1)
    return final

def countArray3(n, k, x):#Dynamic approach in order O(kn)
    a=[[0 for i in range(k+1) ] for j in range(n+1)]
    a[1][1]=1
    for i in range(2,n+1):
        for j in range(1,k+1):
            for k in range(1,k+1):
                if(k!=j):
                    a[i][j]=(a[i][j]+a[i-1][k])%(10**9+7)

    return a[n][x]%(10**9+7)

def countArray(n, k, x): #compress dynamic approach in order O(n)
    a = [[0 for i in range(3)] for j in range(n + 1)]
    a[1][1] = 1
    for i in range(2, n + 1):
        a[i][1]=(a[i-1][2]*(k-1))%(10**9+7)
        a[i][2]=(a[i-1][2]*(k-2)+a[i-1][1])%(10**9+7)
    if(x==1):
        return a[n][1]%(10**9+7)
    else:
        return a[n][2]%(10**9+7)

if __name__ == '__main__':
    fptr = open('results.txt', 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
