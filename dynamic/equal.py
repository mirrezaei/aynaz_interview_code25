#!/bin/python3
#UNSOLVED
import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(arr):
    o=0
    for c in [1,2,5]:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if(j!=i):
                    arr[j]=arr[j]+c
                    o=o+1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
