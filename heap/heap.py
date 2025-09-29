#This question is designed to help you get a better understanding of basic heap operations.
#You will be given queries of  types:

#"1 v " - Add an element  to the heap.
#"2 v " - Delete the element  from the heap.
#"3" - Print the minimum of all the elements in the heap.

#Input Format

#The first line contains the number of queries, Q.
#Each of the next Q lines contains a single query of any one of the  above mentioned types.


#Output Format

#For each query of type 3, print the minimum value on a single line.

import heapq

n=int(raw_input())

h=[]
for i in range(n):
    query=map(int, raw_input().strip().split(' '))
    if(len(query)==2):
        if(query[0]==1):
            heapq.heappush(h,query[1])
        else:
            h.remove(query[1])
            heapq.heapify(h)
    else:
        print(h)
        print(int(h[0]))
