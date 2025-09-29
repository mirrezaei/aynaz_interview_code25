#You are given a list of N positive integers, A = {a[1], a[2], ..., a[N]} and another integer S. You have to find whether there exists a non-empty subset of A whose sum is greater than or equal to S.

#You have to print the size of minimal subset whose sum is greater than or equal to S. If there exists no such subset then print -1 instead.

#Input
#First line will contain an integer, N, which is the size of list A. Second line contains N space separated integers, representing the elements of list A. In third line there is an integer, T, which represent the number of test cases to follow. Then follows T lines. Each one of them contains an single integer, S.

#Output
#For each test case, print the size of minimal subset whose sum is greater than or equal to S. If there's no such subset then print -1.

import sys

print("Enter the length of the list:")
m=map(int,raw_input().strip().split(' '))[0]
print("Enter the list:")
A=map(int,raw_input().strip().split(' '))
print("Enter the number of test cases:")
t=int(raw_input().strip().split(' ')[0])
testCases=[]
for i in range(t):
    testCases.append(int(raw_input().strip().split(' ')[0]))


def minSizeEqualSubset():
    for t in testCases:
        sizeSubsetSum=[[0 for j in range(m+1)] for i in range(t+1)]
        for i in range(m+1):
            sizeSubsetSum[0][i]=0#the size of minimal subset to reach t=0 using numbers[:i] is 0

        for i in range(t+1):
            sizeSubsetSum[i][0]=sys.maxint#the size of minimal subset to reach t is

        for i in range(1,t+1):
            for j in range(1,m+1):
                if(i-A[j-1]>=0):
                    sizeSubsetSum[i][j]=min(sizeSubsetSum[i-A[j-1]][j-1]+1,sizeSubsetSum[i][j-1])
                else:
                    sizeSubsetSum[i][j]=sizeSubsetSum[i][j-1]
        if sizeSubsetSum[t][m]==sys.maxint:
            print(-1)
        else:
            print(sizeSubsetSum[t][m])

#sizeSubsetSum[i][j]: the size of minimal subset to reach i using first j elements in sequence
#sizeSubsetSum[i-A[j-1]][j-1]+1 : use the jth element
# sizeSubsetSum[i][j-1] don't use the jth element

def minSizeEqualGreaterSubset():
    for t in testCases:
        sizeSubsetSum=[[0 for j in range(m+1)] for i in range(t+1)]
        for i in range(m+1):
            sizeSubsetSum[0][i]=0

        for i in range(t+1):
            sizeSubsetSum[i][0]=sys.maxint

        for i in range(1,t+1):
            for j in range(1,m+1):
                if(i-A[j-1]>=0):
                    sizeSubsetSum[i][j]=min(sizeSubsetSum[i-A[j-1]][j-1]+1,sizeSubsetSum[i][j-1])
                else:
                    sizeSubsetSum[i][j]=min(1,sizeSubsetSum[i][j-1])

        if sizeSubsetSum[t][m]==sys.maxint:
            print(-1)
        else:
            print(sizeSubsetSum[t][m])


minSizeEqualGreaterSubset()